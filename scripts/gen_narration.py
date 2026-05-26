"""
Generate narration audio for the Pax Mushin video using ElevenLabs TTS.

Reads the script markdown, extracts narrator lines (WIZ),
splits into chunks under the ElevenLabs character limit,
generates MP3 per chunk, then concatenates with ffmpeg.

Usage:
    python scripts/gen_narration.py
"""

import argparse
import os
import re
import sys
import subprocess
import time

# --------------- config ---------------
SCRIPT_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "gestos",
    "_backlog",
    "video-educativo",
    "script-mushin-pax-9min.md",
)
DEFAULT_AUDIO_DIR = os.path.join(
    os.path.dirname(__file__),
    "..",
    "gestos",
    "_backlog",
    "video-educativo",
    "audio",
)

DEFAULT_VOICE_ID = "B52raBK48m23qWYbwchQ"
VOICE_ID = DEFAULT_VOICE_ID  # will be overridden by CLI args
MAX_CHARS_PER_CHUNK = 4800  # ElevenLabs limit ~5000, leave margin
MODEL_ID = "eleven_multilingual_v2"

# Voice settings tuned for wise old narrator
VOICE_SETTINGS = {
    "stability": 0.50,
    "similarity_boost": 0.75,
    "style": 0.30,
}

# --------------- helpers ---------------

def load_api_key() -> str:
    """Load ElevenLabs API key from .env file."""
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    env_local_path = os.path.join(os.path.dirname(__file__), "..", ".env.local")

    for path in [env_local_path, env_path]:
        path = os.path.normpath(path)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip()
                if key in (
                    "ELEVENLABS_API_KEY",
                    "ELEVEN_LABS_API_KEY",
                    "ELEVEN_API_KEY",
                ):
                    return value
    # Fallback to environment variable
    for name in ("ELEVENLABS_API_KEY", "ELEVEN_LABS_API_KEY", "ELEVEN_API_KEY"):
        val = os.environ.get(name)
        if val:
            return val
    print("ERROR: No ElevenLabs API key found in .env files or environment.")
    sys.exit(1)


def extract_narration(md_path: str) -> list[tuple[str, str]]:
    """
    Extract narrator lines from the script markdown.
    Returns list of (section_label, narration_text) tuples.
    """
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match section headers like ## [00:00] HOOK, ## [00:40] PART ONE ...
    section_pattern = re.compile(r"^## \[[\d:]+\]\s+(.+)$", re.MULTILINE)
    narrator_pattern = re.compile(
        r"^NARRATOR\s*\(WIZ\)\s*:\s*(.+?)(?=\n\n|\n\[|\nNARRATOR|\n---|\n##|\Z)",
        re.MULTILINE | re.DOTALL,
    )

    sections = list(section_pattern.finditer(content))
    results = []

    for i, sec_match in enumerate(sections):
        sec_name = sec_match.group(1).strip()
        start = sec_match.start()
        end = sections[i + 1].start() if i + 1 < len(sections) else len(content)
        section_text = content[start:end]

        narr_lines = []
        for nm in narrator_pattern.finditer(section_text):
            text = nm.group(1).strip()
            # Clean up any remaining markdown artifacts
            text = re.sub(r"\s+", " ", text)
            narr_lines.append(text)

        if narr_lines:
            results.append((sec_name, " ".join(narr_lines)))

    return results


def chunk_sections(
    sections: list[tuple[str, str]], max_chars: int
) -> list[tuple[str, str]]:
    """
    Merge sections into chunks that fit within max_chars.
    Each chunk gets a label like 'part-01', 'part-02', etc.
    """
    chunks = []
    current_text = ""
    current_labels = []
    chunk_num = 1

    for label, text in sections:
        # If adding this section would exceed limit, flush current chunk
        if current_text and len(current_text) + len(text) + 2 > max_chars:
            chunks.append((f"part-{chunk_num:02d}", current_text.strip()))
            chunk_num += 1
            current_text = ""
            current_labels = []

        # If a single section exceeds limit, split it by sentences
        if len(text) > max_chars:
            if current_text:
                chunks.append((f"part-{chunk_num:02d}", current_text.strip()))
                chunk_num += 1
                current_text = ""
                current_labels = []

            sentences = re.split(r"(?<=[.!?])\s+", text)
            buf = ""
            for sent in sentences:
                if buf and len(buf) + len(sent) + 1 > max_chars:
                    chunks.append((f"part-{chunk_num:02d}", buf.strip()))
                    chunk_num += 1
                    buf = ""
                buf += " " + sent
            if buf.strip():
                current_text = buf
                current_labels = [label]
        else:
            current_text += " " + text
            current_labels.append(label)

    if current_text.strip():
        chunks.append((f"part-{chunk_num:02d}", current_text.strip()))

    return chunks


def generate_audio(api_key: str, text: str, output_path: str) -> bool:
    """Call ElevenLabs TTS API and save the audio file."""
    import requests

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    data = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": VOICE_SETTINGS,
    }

    print(f"  Sending {len(text)} chars to ElevenLabs...")
    resp = requests.post(url, headers=headers, json=data, timeout=120)

    if resp.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(resp.content)
        size_kb = len(resp.content) / 1024
        print(f"  Saved: {output_path} ({size_kb:.0f} KB)")
        return True
    else:
        print(f"  ERROR {resp.status_code}: {resp.text[:500]}")
        return False


def concatenate_chunks(audio_dir: str, chunk_files: list[str], output_name: str):
    """Concatenate MP3 chunks using ffmpeg."""
    if len(chunk_files) <= 1:
        print("Single chunk — no concatenation needed.")
        return

    list_file = os.path.join(audio_dir, "concat_list.txt")
    with open(list_file, "w", encoding="utf-8") as f:
        for cf in chunk_files:
            # ffmpeg concat needs forward slashes or escaped backslashes
            safe_path = os.path.basename(cf)
            f.write(f"file '{safe_path}'\n")

    output_path = os.path.join(audio_dir, output_name)
    cmd = [
        "ffmpeg",
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        list_file,
        "-c",
        "copy",
        output_path,
    ]
    print(f"\nConcatenating {len(chunk_files)} chunks into {output_name}...")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=audio_dir)
    if result.returncode == 0:
        size_mb = os.path.getsize(output_path) / (1024 * 1024)
        print(f"  Success: {output_path} ({size_mb:.1f} MB)")
    else:
        print(f"  ffmpeg error: {result.stderr[:500]}")

    # Clean up list file
    os.remove(list_file)


# --------------- main ---------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate narration audio for Pax Mushin video using ElevenLabs TTS."
    )
    parser.add_argument(
        "--voice-id",
        default=DEFAULT_VOICE_ID,
        help=f"ElevenLabs voice ID (default: {DEFAULT_VOICE_ID})",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help=f"Output directory for audio files (default: gestos/_backlog/video-educativo/audio)",
    )
    args = parser.parse_args()

    # Override global VOICE_ID with CLI arg
    global VOICE_ID
    VOICE_ID = args.voice_id

    audio_dir = os.path.normpath(args.output_dir) if args.output_dir else os.path.normpath(DEFAULT_AUDIO_DIR)

    print("=" * 60)
    print("Pax Mushin Video — Narration Generator (ElevenLabs)")
    print(f"  Voice ID: {VOICE_ID}")
    print(f"  Output:   {audio_dir}")
    print("=" * 60)

    api_key = load_api_key()
    print(f"API key loaded: {api_key[:8]}...{api_key[-4:]}")

    script_path = os.path.normpath(SCRIPT_PATH)
    print(f"\nReading script: {script_path}")
    sections = extract_narration(script_path)

    total_chars = sum(len(t) for _, t in sections)
    print(f"Extracted {len(sections)} sections, {total_chars} chars total")
    for label, text in sections:
        print(f"  [{label}] {len(text)} chars")

    chunks = chunk_sections(sections, MAX_CHARS_PER_CHUNK)
    print(f"\nSplit into {len(chunks)} chunks for API calls:")
    for label, text in chunks:
        print(f"  [{label}] {len(text)} chars")

    os.makedirs(audio_dir, exist_ok=True)

    # Write narration text to file for reference
    narr_text_path = os.path.join(audio_dir, "narration-text.txt")
    with open(narr_text_path, "w", encoding="utf-8") as f:
        for label, text in chunks:
            f.write(f"=== {label} ({len(text)} chars) ===\n")
            f.write(text)
            f.write("\n\n")
    print(f"\nNarration text saved: {narr_text_path}")

    # Generate audio for each chunk
    chunk_files = []
    for i, (label, text) in enumerate(chunks):
        output_path = os.path.join(audio_dir, f"narration-{label}.mp3")
        print(f"\n[{i+1}/{len(chunks)}] Generating {label}...")
        success = generate_audio(api_key, text, output_path)
        if success:
            chunk_files.append(output_path)
        else:
            print(f"  FAILED — stopping. Generated {len(chunk_files)} chunks so far.")
            break

        # Brief pause between API calls to avoid rate limiting
        if i < len(chunks) - 1:
            time.sleep(1)

    if chunk_files:
        concatenate_chunks(audio_dir, chunk_files, "narration-full.mp3")

    # Estimate duration (~150 words per minute for narration)
    word_count = sum(len(t.split()) for _, t in chunks)
    est_minutes = word_count / 150
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  Chunks generated: {len(chunk_files)}/{len(chunks)}")
    print(f"  Total words: {word_count}")
    print(f"  Estimated duration: {est_minutes:.1f} minutes")
    print(f"  Audio files: {audio_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
