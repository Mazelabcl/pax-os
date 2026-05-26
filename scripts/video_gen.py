"""
video_gen.py — Multi-backend I2V (Image-to-Video) generator for Pax.

Supports 7 models, ALL via Replicate API (REPLICATE_API_TOKEN):
  - wan           → wavespeedai/wan-2.1-i2v-720p
  - grok          → xai/grok-imagine-video
  - kling-v3-omni → kwaivgi/kling-v3-omni-video
  - kling-v3      → kwaivgi/kling-v3-video
  - kling-v2.5-turbo → kwaivgi/kling-v2.5-turbo-pro
  - kling-o1      → kwaivgi/kling-o1
  - kling-v2.6    → kwaivgi/kling-v2.6

Usage (CLI):
    python scripts/video_gen.py --start frame1.png --prompt "..." --model wan --duration 5 --output out.mp4
    python scripts/video_gen.py --start f1.png --end f2.png --prompt "..." --model kling-v3-omni --duration 5
    python scripts/video_gen.py --start f1.png --prompt "..." --model grok --duration 10 --output out.mp4

Usage (import):
    from scripts.video_gen import generate_video
    import asyncio
    path = asyncio.run(generate_video("frame.png", prompt="...", model="kling-v3"))

Requires:
    - requests (pip install requests)
    - REPLICATE_API_TOKEN in .env or .env.local
"""

import os
import sys
import time
import base64
import argparse
import asyncio
import re

# Reuse _load_env from openai_images (loads .env / .env.local without python-dotenv)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openai_images import _load_env  # noqa: E402

try:
    import requests
except ImportError as e:
    raise ImportError("requests is not installed. Run: pip install requests") from e


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

REPLICATE_API_BASE = "https://api.replicate.com/v1"

# Model registry: short name -> Replicate slug
MODEL_SLUGS = {
    "wan":              "wavespeedai/wan-2.1-i2v-720p",
    "grok":             "xai/grok-imagine-video",
    "kling-v3-omni":    "kwaivgi/kling-v3-omni-video",
    "kling-v3":         "kwaivgi/kling-v3-video",
    "kling-v2.5-turbo": "kwaivgi/kling-v2.5-turbo-pro",
    "kling-o1":         "kwaivgi/kling-o1",
    "kling-v2.6":       "kwaivgi/kling-v2.6",
}

ALL_MODELS = list(MODEL_SLUGS.keys())

POLL_INTERVAL_S = 5
POLL_TIMEOUT_S = 600  # 10 min


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _load_keys():
    """Load environment variables from .env / .env.local."""
    _load_env()


def _get_replicate_token() -> str:
    token = os.environ.get("REPLICATE_API_TOKEN", "").strip()
    if not token:
        raise EnvironmentError(
            "REPLICATE_API_TOKEN not set. Add it to .env or .env.local:\n"
            "  REPLICATE_API_TOKEN=r8_...\n"
            "Get token at: https://replicate.com/account/api-tokens"
        )
    return token


def _replicate_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def _mime_for(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(ext, "image/png")


def _image_to_data_url(path: str) -> str:
    """Encode local image as data URL for API consumption."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Image not found: {path}")
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = _mime_for(path)
    return f"data:{mime};base64,{b64}"


# ---------------------------------------------------------------------------
# Replicate generic prediction engine
# ---------------------------------------------------------------------------

def _check_replicate_response(resp):
    """Check Replicate HTTP response for common errors."""
    if resp.status_code == 401:
        raise RuntimeError("401 Unauthorized — REPLICATE_API_TOKEN invalid or expired.")
    if resp.status_code == 402:
        raise RuntimeError("402 Payment Required — no credit on Replicate.")
    if resp.status_code == 422:
        raise RuntimeError(f"422 Unprocessable Entity — {resp.text}")
    if resp.status_code == 429:
        raise RuntimeError("429 Rate Limit — too many requests. Wait and retry.")
    resp.raise_for_status()


def _poll_replicate(get_url: str, token: str, prediction_id: str, model_tag: str) -> dict:
    """Poll a Replicate prediction until done."""
    deadline = time.time() + POLL_TIMEOUT_S
    last_status = None
    while time.time() < deadline:
        time.sleep(POLL_INTERVAL_S)
        poll = requests.get(get_url, headers=_replicate_headers(token), timeout=30)
        poll.raise_for_status()
        prediction = poll.json()
        status = prediction.get("status", "")
        if status != last_status:
            print(f"[{model_tag}] status: {status}")
            last_status = status
        if status == "succeeded":
            return prediction
        if status in ("failed", "canceled"):
            err = prediction.get("error") or prediction
            raise RuntimeError(f"[{model_tag}] Prediction {prediction_id} failed ({status}): {err}")
    raise RuntimeError(f"[{model_tag}] Timeout: prediction {prediction_id} did not finish in {POLL_TIMEOUT_S}s")


def _extract_video_url(prediction: dict) -> str:
    """Extract video URL from Replicate prediction output (handles multiple formats)."""
    output = prediction.get("output")
    if isinstance(output, str):
        return output
    if isinstance(output, list) and output:
        first = output[0]
        if isinstance(first, str):
            return first
        if isinstance(first, dict):
            return first.get("url") or first.get("video") or ""
    if isinstance(output, dict):
        return output.get("video") or output.get("url") or ""
    return ""


def _download_video(url: str, output_path: str, model_tag: str) -> str:
    """Download mp4 from URL to output_path."""
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    print(f"[{model_tag}] Downloading -> {output_path}")
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"[{model_tag}] Done: {size_mb:.1f} MB -> {output_path}")
    return output_path


def _run_prediction(model_tag: str, model_slug: str, model_input: dict, output_path: str) -> str:
    """Create prediction, poll, download video. Generic for all Replicate models."""
    token = _get_replicate_token()

    print(f"[{model_tag}] Creating prediction — model={model_slug}")
    prompt_preview = model_input.get("prompt", "")[:80]
    print(f"[{model_tag}] Prompt: {prompt_preview}{'...' if len(model_input.get('prompt', '')) > 80 else ''}")

    create_url = f"{REPLICATE_API_BASE}/models/{model_slug}/predictions"
    resp = requests.post(
        create_url,
        headers=_replicate_headers(token),
        json={"input": model_input},
        timeout=60,
    )
    _check_replicate_response(resp)
    prediction = resp.json()

    prediction_id = prediction.get("id")
    get_url = prediction.get("urls", {}).get("get") or f"{REPLICATE_API_BASE}/predictions/{prediction_id}"
    print(f"[{model_tag}] prediction id={prediction_id}")

    result = _poll_replicate(get_url, token, prediction_id, model_tag)
    video_url = _extract_video_url(result)
    if not video_url:
        raise RuntimeError(f"[{model_tag}] Job completed but no video URL. Output: {result.get('output')}")

    return _download_video(video_url, output_path, model_tag)


# ---------------------------------------------------------------------------
# Model-specific input builders
# ---------------------------------------------------------------------------

def _build_wan_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for wavespeedai/wan-2.1-i2v-720p."""
    inp = {
        "prompt": prompt,
        "image": _image_to_data_url(start_frame),
        "aspect_ratio": "16:9",
        "sample_steps": 30,
    }
    if end_frame:
        # Wan I2V does not natively support end-frame; append hint to prompt
        inp["prompt"] += " Transition ends matching the final composition."
    return inp


def _build_grok_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for xai/grok-imagine-video."""
    inp = {
        "prompt": prompt,
        "duration": min(duration, 15),
        "resolution": "720p",
        "aspect_ratio": "16:9",
    }
    if start_frame:
        inp["image"] = _image_to_data_url(start_frame)
    # Grok does not support end_frame
    if end_frame:
        print("[grok] WARNING: end_frame not supported by Grok, ignoring.")
    return inp


def _build_kling_v3_omni_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for kwaivgi/kling-v3-omni-video."""
    inp = {
        "prompt": prompt,
        "duration": max(3, min(duration, 15)),
        "mode": "pro",  # 1080p
        "aspect_ratio": "16:9",
        "generate_audio": False,
    }
    if start_frame:
        inp["start_image"] = _image_to_data_url(start_frame)
    if end_frame:
        inp["end_image"] = _image_to_data_url(end_frame)
    return inp


def _build_kling_v3_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for kwaivgi/kling-v3-video."""
    inp = {
        "prompt": prompt,
        "duration": max(3, min(duration, 15)),
        "mode": "pro",  # 1080p
        "aspect_ratio": "16:9",
        "generate_audio": False,
    }
    if start_frame:
        inp["start_image"] = _image_to_data_url(start_frame)
    if end_frame:
        inp["end_image"] = _image_to_data_url(end_frame)
    return inp


def _build_kling_v25_turbo_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for kwaivgi/kling-v2.5-turbo-pro."""
    inp = {
        "prompt": prompt,
        "duration": max(5, min(duration, 10)),  # only 5 or 10
        "aspect_ratio": "16:9",
    }
    if start_frame:
        inp["start_image"] = _image_to_data_url(start_frame)
    if end_frame:
        inp["end_image"] = _image_to_data_url(end_frame)
    return inp


def _build_kling_o1_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for kwaivgi/kling-o1."""
    inp = {
        "prompt": prompt,
        "duration": max(5, min(duration, 10)),  # 5 or 10
        "mode": "pro",
        "aspect_ratio": "16:9",
    }
    if start_frame:
        inp["start_image"] = _image_to_data_url(start_frame)
    if end_frame:
        inp["end_image"] = _image_to_data_url(end_frame)
    return inp


def _build_kling_v26_input(start_frame: str, end_frame: str | None, prompt: str, duration: int) -> dict:
    """Build input for kwaivgi/kling-v2.6."""
    inp = {
        "prompt": prompt,
        "duration": max(5, min(duration, 10)),  # 5 or 10
        "aspect_ratio": "16:9",
        "generate_audio": False,
    }
    if start_frame:
        inp["start_image"] = _image_to_data_url(start_frame)
    # v2.6 does not support end_image
    if end_frame:
        print("[kling-v2.6] WARNING: end_frame not supported by Kling v2.6, ignoring.")
    return inp


# Map model name -> (input builder, slug)
INPUT_BUILDERS = {
    "wan":              _build_wan_input,
    "grok":             _build_grok_input,
    "kling-v3-omni":    _build_kling_v3_omni_input,
    "kling-v3":         _build_kling_v3_input,
    "kling-v2.5-turbo": _build_kling_v25_turbo_input,
    "kling-o1":         _build_kling_o1_input,
    "kling-v2.6":       _build_kling_v26_input,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def generate_video(
    start_frame: str,
    end_frame: str = None,
    prompt: str = "",
    output_path: str = "output.mp4",
    duration: int = 5,
    model: str = "wan",
) -> str:
    """
    Generate a video clip from start (and optionally end) frame images.

    Args:
        start_frame:  Path to start image.
        end_frame:    Path to end image (optional, model-dependent).
        prompt:       Motion/action description.
        output_path:  Where to save the .mp4.
        duration:     Clip duration in seconds (5 or 10 typical).
        model:        One of: wan, grok, kling-v3-omni, kling-v3,
                      kling-v2.5-turbo, kling-o1, kling-v2.6.

    Returns:
        Path to the downloaded .mp4.
    """
    _load_keys()

    if model not in MODEL_SLUGS:
        raise ValueError(
            f"Unknown model: '{model}'. "
            f"Available: {', '.join(ALL_MODELS)}"
        )

    start_frame = os.path.abspath(start_frame)
    if end_frame:
        end_frame = os.path.abspath(end_frame)
    output_path = os.path.abspath(output_path)

    builder = INPUT_BUILDERS[model]
    model_input = builder(start_frame, end_frame, prompt, duration)
    slug = MODEL_SLUGS[model]

    # Run in thread to avoid blocking event loop (requests is sync)
    return await asyncio.to_thread(
        _run_prediction, model, slug, model_input, output_path
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Pax multi-backend I2V video generator (7 models via Replicate)"
    )
    parser.add_argument("--start", required=True, help="Path to start frame image")
    parser.add_argument("--end", default=None, help="Path to end frame image (optional)")
    parser.add_argument("--prompt", default="", help="Motion/action description")
    parser.add_argument("--output", default="output.mp4", help="Output .mp4 path")
    parser.add_argument("--duration", type=int, default=5, help="Duration in seconds (default 5)")
    parser.add_argument(
        "--model", choices=ALL_MODELS, default="wan",
        help=f"Model backend (default: wan). Options: {', '.join(ALL_MODELS)}"
    )
    args = parser.parse_args()

    path = asyncio.run(generate_video(
        start_frame=args.start,
        end_frame=args.end,
        prompt=args.prompt,
        output_path=args.output,
        duration=args.duration,
        model=args.model,
    ))
    print(f"\nVideo saved: {path}")


if __name__ == "__main__":
    main()
