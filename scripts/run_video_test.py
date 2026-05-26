"""
Run test video generation for 2 scenes x 2 models (Wan + Kling).
Saves 4 clips to gestos/_backlog/video-educativo/test-clips/.
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from video_gen import generate_video, _load_keys, _get_replicate_token, _get_fal_key

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAMES_DIR = os.path.join(REPO_ROOT, "gestos", "_backlog", "video-educativo", "frames-9min")
OUTPUT_DIR = os.path.join(REPO_ROOT, "gestos", "_backlog", "video-educativo", "test-clips")

SCENES = [
    {
        "name": "scene-03",
        "start": os.path.join(FRAMES_DIR, "scene-03-start.png"),
        "end": os.path.join(FRAMES_DIR, "scene-03-end.png"),
        "prompt": "The wise elder Pax character gestures while explaining a concept, crystal on his staff glows brighter, camera slowly pushes in, magical particles float",
        "duration": 5,
    },
    {
        "name": "scene-07",
        "start": os.path.join(FRAMES_DIR, "scene-07-start.png"),
        "end": os.path.join(FRAMES_DIR, "scene-07-end.png"),
        "prompt": "Young turquoise cyclops character sits cross-legged trying to focus, the crystal in front dims and flickers, slight frustrated head movement",
        "duration": 5,
    },
]


async def run_all():
    _load_keys()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    has_replicate = bool(_get_replicate_token())
    has_fal = bool(_get_fal_key())

    if not has_replicate:
        print("[WARN] REPLICATE_API_TOKEN not found — skipping Wan.")
    if not has_fal:
        print("[WARN] FAL_KEY not found — skipping Kling.")

    if not has_replicate and not has_fal:
        print("[ERROR] No API keys found. Add REPLICATE_API_TOKEN and/or FAL_KEY to .env or .env.local")
        return

    results = []
    for scene in SCENES:
        for model_name in ["wan", "kling"]:
            if model_name == "wan" and not has_replicate:
                continue
            if model_name == "kling" and not has_fal:
                continue

            out_path = os.path.join(OUTPUT_DIR, f"{scene['name']}-{model_name}.mp4")
            print(f"\n{'='*60}")
            print(f"Generating: {scene['name']} with {model_name}")
            print(f"{'='*60}")
            try:
                path = await generate_video(
                    start_frame=scene["start"],
                    end_frame=scene["end"],
                    prompt=scene["prompt"],
                    output_path=out_path,
                    duration=scene["duration"],
                    model=model_name,
                )
                results.append((scene["name"], model_name, "OK", path))
                print(f"[OK] {path}")
            except Exception as e:
                results.append((scene["name"], model_name, "FAIL", str(e)))
                print(f"[FAIL] {scene['name']}-{model_name}: {e}")

    print(f"\n{'='*60}")
    print("RESULTS SUMMARY")
    print(f"{'='*60}")
    for scene_name, model_name, status, detail in results:
        print(f"  {scene_name}-{model_name}: {status} — {detail}")


if __name__ == "__main__":
    asyncio.run(run_all())
