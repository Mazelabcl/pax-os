"""
produce_mushin.py — Master production script for the 9-minute Mushin Pax video.

Strategy ("recursera" / low budget):
  - 7 scenes animated with Kling v2.6 via Replicate (~$2.45 USD)
  - 12 scenes with Ken Burns effects via ffmpeg (free)
  - Concatenate 19 clips + audio = final video

Usage:
    # Full pipeline (animated + kenburns + composite)
    python gestos/_backlog/video-educativo/produce_mushin.py --all

    # Only Ken Burns clips (no API cost)
    python gestos/_backlog/video-educativo/produce_mushin.py --kenburns

    # Only animated clips (API cost ~$2.45)
    python gestos/_backlog/video-educativo/produce_mushin.py --animated

    # Only composite (assumes clips already exist)
    python gestos/_backlog/video-educativo/produce_mushin.py --composite

    # Dry run (show what would be done)
    python gestos/_backlog/video-educativo/produce_mushin.py --all --dry-run
"""

import os
import sys
import subprocess
import asyncio
import argparse
import json
import random
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.resolve()
FRAMES_DIR = BASE_DIR / "frames-9min"
CLIPS_DIR = BASE_DIR / "clips"
FINAL_DIR = BASE_DIR / "final"
AUDIO_DIR = BASE_DIR / "audio"
AUDIO_MYRRDIN_DIR = BASE_DIR / "audio-myrrdin"

# Add scripts dir to path for video_gen import
# BASE_DIR = .../pax-os/gestos/_backlog/video-educativo
# parents[0] = _backlog, parents[1] = gestos, parents[2] = pax-os
REPO_ROOT = BASE_DIR.parents[2]  # pax-os/
sys.path.insert(0, str(REPO_ROOT / "scripts"))

# ffmpeg path (use system ffmpeg)
FFMPEG = "ffmpeg"
FFPROBE = "ffprobe"

# ---------------------------------------------------------------------------
# Scene definitions
# ---------------------------------------------------------------------------

# Scenes to animate with Kling v2.6 (7 scenes)
ANIMATED_SCENES = [1, 5, 8, 11, 14, 17, 19]

# Scenes for Ken Burns effects (12 scenes)
KENBURNS_SCENES = [2, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18]

# Storyboard prompts for animated scenes (extracted from storyboard-9min.md)
ANIMATED_PROMPTS = {
    1: (
        "A single ancient crystal in a black void pulses with faint jade light, then the pulse dies completely. "
        "The crystal cracks and goes dark. 3D PBR style, volumetric fog, subsurface scattering. "
        "Camera slowly pushes in. Mood: ominous, loss, urgency. Palette: charcoal with jade whisper."
    ),
    5: (
        "Jiggy, a turquoise-skinned creature with a single large eye, explores deep luminous tunnels. "
        "Bioluminescent plants hang like chandeliers. He crouches near a violet-gold mineral vein in pure awe. "
        "3D PBR neon-magic style, amber and magenta veins glow in basalt walls. "
        "Camera slowly tracks forward. Mood: discovery, wonder, timelessness."
    ),
    8: (
        "A chaotic alcove filled with scattered objects — maps, food, crystal fragments. "
        "Jiggy, turquoise-skinned with single eye, sits trying to charge a crystal. "
        "KZ, a small bioluminescent lime creature, jumps on his shoulder, breaking concentration. "
        "The crystal's glow dies. 3D PBR style. Camera slow zoom to his frustrated hands. "
        "Mood: sabotage by environment, visual overwhelm."
    ),
    11: (
        "A sacred chamber with seven beautiful alchemical instruments arranged on a table. "
        "Each tool glows with a different color — amber, jade, brass, iridescent. "
        "In the center, one crystal sits completely dark, ignored. "
        "Camera slowly tightens on the dark crystal surrounded by glowing tools. "
        "3D PBR neon-magic. Mood: ironic productivity, the subtraction problem visualized."
    ),
    14: (
        "Jiggy sits in a minimal chamber, hands on a crystal, but his body vibrates visibly. "
        "Magenta energy distortion flickers around his silhouette. The crystal stutters between glow and dark. "
        "Close-up on hands — jade glow stutters, magenta sparks escape upward. "
        "3D PBR style, volumetric fog. Camera pushes to extreme close-up on hands. "
        "Mood: caged energy, body-mind disconnect made visible."
    ),
    17: (
        "Tuesday morning. Jiggy enters his bare chamber, already having run. "
        "He sits, places hands on crystal — no hesitation. Seven crystals charge in sequence. "
        "Full spectrum light fills the room: jade, amber, magenta, gold, all blazing. "
        "Jiggy grins, stunned by effortless mastery. KZ peeks through the door and backs away. "
        "3D PBR neon-magic. Camera pulls back to reveal the full light show. "
        "Mood: triumph, Mushin achieved, effortless flow."
    ),
    19: (
        "Return to the opening crystal — same angle, same void. But now it BLAZES with jade, gold, magenta light. "
        "The crack from Scene 01 is still there, but light bleeds through it beautifully. "
        "Camera holds, then slowly reveals Wiz — amber-skinned elder with white beard, staff with violet crystal. "
        "He looks directly at the viewer. Behind him, the Pax logo materializes in jade light. "
        "3D PBR neon-magic. Mood: resurrection, call to action, quiet power."
    ),
}

# Duration targets per scene (seconds)
SCENE_DURATIONS = {
    1: 10, 2: 10, 3: 10, 4: 30, 5: 20, 6: 20, 7: 30,
    8: 30, 9: 20, 10: 40, 11: 30, 12: 40, 13: 20,
    14: 30, 15: 30, 16: 30, 17: 30, 18: 20, 19: 20,
}

# Ken Burns effects to cycle through
KB_EFFECTS = [
    "zoom_in",
    "zoom_out",
    "pan_left_to_right",
    "pan_right_to_left",
    "crossfade",
]

# Assign effects to Ken Burns scenes for variety
KB_SCENE_EFFECTS = {
    2: "zoom_out",        # Uray Pacha revealed — zoom out for grandeur
    3: "crossfade",       # Ancient Pax montage — crossfade start to end
    4: "pan_left_to_right",  # Jiggy's alcove — pan across the mess
    6: "zoom_in",         # Agatha assigns — zoom to Jiggy's face
    7: "crossfade",       # Finds his why — crossfade to crystal glow
    9: "pan_right_to_left",  # Main hall chaos — pan across chaos
    10: "crossfade",      # Sacred chamber — crossfade to charged room
    12: "crossfade",      # Bare hands — crossfade tools away to bare hands
    13: "zoom_in",        # Wiz remembers — zoom to elder's smile
    15: "pan_left_to_right",  # Ancient mural — pan across temple art
    16: "zoom_out",       # Runs tunnels — zoom out for speed feeling
    18: "crossfade",      # Lit corridor — crossfade to Wiz at node map
}


# ---------------------------------------------------------------------------
# Ken Burns ffmpeg generators
# ---------------------------------------------------------------------------

def _get_image_size(img_path: str) -> tuple:
    """Get image width and height via ffprobe."""
    result = subprocess.run(
        [FFPROBE, "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(img_path)],
        capture_output=True, text=True
    )
    w, h = result.stdout.strip().split(",")
    return int(w), int(h)


def _run_ffmpeg(cmd: list, desc: str = ""):
    """Run ffmpeg command and check result."""
    print(f"  [ffmpeg] {desc}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  [ffmpeg] STDERR: {result.stderr[-500:]}")
        raise RuntimeError(f"ffmpeg failed: {desc}")
    return result


def generate_kenburns_zoom_in(start_img: str, output: str, duration: int = 25):
    """Ken Burns zoom-in effect: from full image to center detail."""
    # Output: 1920x1080 at 30fps
    total_frames = duration * 30
    # Zoom from 1.0 to 1.4 over the duration
    zoom_speed = 0.4 / total_frames
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", str(start_img),
        "-vf", (
            f"scale=2560:1440,format=yuv420p,"
            f"zoompan=z='min(zoom+{zoom_speed:.6f},1.4)'"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s=1920x1080:fps=30"
        ),
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-t", str(duration), "-pix_fmt", "yuv420p",
        str(output)
    ]
    _run_ffmpeg(cmd, f"zoom-in {Path(start_img).name} -> {Path(output).name}")


def generate_kenburns_zoom_out(start_img: str, output: str, duration: int = 25):
    """Ken Burns zoom-out: start zoomed in, pull back to full image."""
    total_frames = duration * 30
    zoom_speed = 0.4 / total_frames
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", str(start_img),
        "-vf", (
            f"scale=2560:1440,format=yuv420p,"
            f"zoompan=z='if(eq(on,1),1.4,max(zoom-{zoom_speed:.6f},1.0))'"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s=1920x1080:fps=30"
        ),
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-t", str(duration), "-pix_fmt", "yuv420p",
        str(output)
    ]
    _run_ffmpeg(cmd, f"zoom-out {Path(start_img).name} -> {Path(output).name}")


def generate_kenburns_pan_lr(start_img: str, output: str, duration: int = 25):
    """Pan from left to right across the image."""
    total_frames = duration * 30
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", str(start_img),
        "-vf", (
            f"scale=2560:1440,format=yuv420p,"
            f"zoompan=z='1.2'"
            f":x='(iw-iw/zoom)*on/{total_frames}'"
            f":y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s=1920x1080:fps=30"
        ),
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-t", str(duration), "-pix_fmt", "yuv420p",
        str(output)
    ]
    _run_ffmpeg(cmd, f"pan-L->R {Path(start_img).name} -> {Path(output).name}")


def generate_kenburns_pan_rl(start_img: str, output: str, duration: int = 25):
    """Pan from right to left across the image."""
    total_frames = duration * 30
    cmd = [
        FFMPEG, "-y", "-loop", "1", "-i", str(start_img),
        "-vf", (
            f"scale=2560:1440,format=yuv420p,"
            f"zoompan=z='1.2'"
            f":x='(iw-iw/zoom)*(1-on/{total_frames})'"
            f":y='ih/2-(ih/zoom/2)'"
            f":d={total_frames}:s=1920x1080:fps=30"
        ),
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-t", str(duration), "-pix_fmt", "yuv420p",
        str(output)
    ]
    _run_ffmpeg(cmd, f"pan-R->L {Path(start_img).name} -> {Path(output).name}")


def generate_crossfade(start_img: str, end_img: str, output: str, duration: int = 25):
    """Crossfade from start image to end image over duration. Each image has Ken Burns zoom too."""
    # Strategy: generate two intermediate clips (with zoompan), then xfade them.
    # This avoids the infinite-stream issue with -loop 1 + zoompan + xfade in one pass.
    #
    # Duration math for xfade: output = clip_a_dur + clip_b_dur - fade_dur
    # We want output = duration, so each sub-clip = (duration + fade_dur) / 2
    fade_dur = min(3, duration // 4)  # 3 sec crossfade max, at least 1/4 duration
    sub_dur = (duration + fade_dur) / 2.0  # each sub-clip duration
    sub_frames = int(sub_dur * 30)
    zoom_speed = 0.0002

    # xfade offset = sub_dur - fade_dur (when fade starts in clip A timeline)
    xfade_offset = sub_dur - fade_dur

    # Temp files for intermediate clips
    tmp_a = str(Path(output).parent / f"_tmp_xfade_a_{Path(output).stem}.mp4")
    tmp_b = str(Path(output).parent / f"_tmp_xfade_b_{Path(output).stem}.mp4")

    try:
        # Generate clip A from start image
        cmd_a = [
            FFMPEG, "-y", "-loop", "1", "-i", str(start_img),
            "-vf", (
                f"scale=2560:1440,format=yuv420p,"
                f"zoompan=z='min(zoom+{zoom_speed},1.2)'"
                f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                f":d={sub_frames}:s=1920x1080:fps=30"
            ),
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", f"{sub_dur:.2f}", "-pix_fmt", "yuv420p", tmp_a
        ]
        _run_ffmpeg(cmd_a, f"crossfade part-A {Path(start_img).name} ({sub_dur:.1f}s)")

        # Generate clip B from end image
        cmd_b = [
            FFMPEG, "-y", "-loop", "1", "-i", str(end_img),
            "-vf", (
                f"scale=2560:1440,format=yuv420p,"
                f"zoompan=z='min(zoom+{zoom_speed},1.2)'"
                f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                f":d={sub_frames}:s=1920x1080:fps=30"
            ),
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-t", f"{sub_dur:.2f}", "-pix_fmt", "yuv420p", tmp_b
        ]
        _run_ffmpeg(cmd_b, f"crossfade part-B {Path(end_img).name} ({sub_dur:.1f}s)")

        # xfade the two clips: output duration = sub_dur + sub_dur - fade_dur = duration
        cmd_xfade = [
            FFMPEG, "-y",
            "-i", tmp_a, "-i", tmp_b,
            "-filter_complex",
            f"[0:v][1:v]xfade=transition=fade:duration={fade_dur}:offset={xfade_offset:.2f}[vout]",
            "-map", "[vout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-pix_fmt", "yuv420p",
            str(output)
        ]
        _run_ffmpeg(cmd_xfade, f"crossfade merge {Path(output).name} (target {duration}s)")

    finally:
        # Clean up temp files
        for tmp in [tmp_a, tmp_b]:
            try:
                os.remove(tmp)
            except OSError:
                pass


# Map effect names to generator functions
KB_GENERATORS = {
    "zoom_in": lambda s, e, o, d: generate_kenburns_zoom_in(s, o, d),
    "zoom_out": lambda s, e, o, d: generate_kenburns_zoom_out(s, o, d),
    "pan_left_to_right": lambda s, e, o, d: generate_kenburns_pan_lr(s, o, d),
    "pan_right_to_left": lambda s, e, o, d: generate_kenburns_pan_rl(s, o, d),
    "crossfade": lambda s, e, o, d: generate_crossfade(s, e, o, d),
}


# ---------------------------------------------------------------------------
# Animated clip generation (Kling v2.6 via Replicate)
# ---------------------------------------------------------------------------

async def generate_animated_clips(dry_run: bool = False):
    """Generate 7 animated clips with Kling v2.6."""
    from video_gen import generate_video

    results = []
    total_cost = 0.0

    for scene_num in ANIMATED_SCENES:
        start_frame = FRAMES_DIR / f"scene-{scene_num:02d}-start.png"
        end_frame = FRAMES_DIR / f"scene-{scene_num:02d}-end.png"
        output = CLIPS_DIR / f"scene-{scene_num:02d}-animated.mp4"
        prompt = ANIMATED_PROMPTS[scene_num]

        if output.exists():
            print(f"[scene-{scene_num:02d}] SKIP — already exists: {output.name}")
            results.append({"scene": scene_num, "status": "skipped", "file": str(output)})
            continue

        duration = 5  # 5 sec per animated clip
        cost = duration * 0.07  # $0.07/sec estimate for Kling v2.6
        total_cost += cost

        if dry_run:
            print(f"[scene-{scene_num:02d}] DRY RUN — would generate {duration}s clip (~${cost:.2f})")
            print(f"  Prompt: {prompt[:80]}...")
            results.append({"scene": scene_num, "status": "dry_run", "cost": cost})
            continue

        print(f"\n{'='*60}")
        print(f"[scene-{scene_num:02d}] Generating {duration}s animated clip (~${cost:.2f})")
        print(f"{'='*60}")

        try:
            # Kling v2.6 does NOT support end_frame, so only pass start
            path = await generate_video(
                start_frame=str(start_frame),
                end_frame=None,  # v2.6 ignores end_frame
                prompt=prompt,
                output_path=str(output),
                duration=duration,
                model="kling-v2.6",
            )
            results.append({"scene": scene_num, "status": "ok", "file": path, "cost": cost})
            print(f"[scene-{scene_num:02d}] OK -> {Path(path).name}")
        except Exception as e:
            print(f"[scene-{scene_num:02d}] ERROR: {e}")
            results.append({"scene": scene_num, "status": "error", "error": str(e), "cost": cost})

    print(f"\n--- Animated clips done. Estimated total cost: ${total_cost:.2f} ---")
    return results


# ---------------------------------------------------------------------------
# Ken Burns clip generation (ffmpeg, free)
# ---------------------------------------------------------------------------

def generate_kenburns_clips(dry_run: bool = False):
    """Generate 12 Ken Burns clips from static frames."""
    results = []

    for scene_num in KENBURNS_SCENES:
        start_frame = FRAMES_DIR / f"scene-{scene_num:02d}-start.png"
        end_frame = FRAMES_DIR / f"scene-{scene_num:02d}-end.png"
        output = CLIPS_DIR / f"scene-{scene_num:02d}-kenburns.mp4"
        effect = KB_SCENE_EFFECTS.get(scene_num, "zoom_in")
        duration = SCENE_DURATIONS.get(scene_num, 25)

        if output.exists():
            print(f"[scene-{scene_num:02d}] SKIP — already exists: {output.name}")
            results.append({"scene": scene_num, "status": "skipped", "effect": effect})
            continue

        if dry_run:
            print(f"[scene-{scene_num:02d}] DRY RUN — {effect}, {duration}s")
            results.append({"scene": scene_num, "status": "dry_run", "effect": effect})
            continue

        print(f"\n[scene-{scene_num:02d}] Generating Ken Burns ({effect}, {duration}s)...")

        try:
            generator = KB_GENERATORS[effect]
            generator(str(start_frame), str(end_frame), str(output), duration)
            results.append({"scene": scene_num, "status": "ok", "effect": effect, "file": str(output)})
            print(f"[scene-{scene_num:02d}] OK -> {output.name}")
        except Exception as e:
            print(f"[scene-{scene_num:02d}] ERROR: {e}")
            results.append({"scene": scene_num, "status": "error", "effect": effect, "error": str(e)})

    return results


# ---------------------------------------------------------------------------
# Normalize clips to same format before concat
# ---------------------------------------------------------------------------

def normalize_clips():
    """Normalize all clips to same resolution/fps/codec for clean concatenation."""
    print("\n=== Normalizing clips to 1920x1080 30fps ===")
    norm_dir = CLIPS_DIR / "normalized"
    norm_dir.mkdir(exist_ok=True)

    for scene_num in range(1, 20):
        # Find the clip (animated or kenburns)
        animated = CLIPS_DIR / f"scene-{scene_num:02d}-animated.mp4"
        kenburns = CLIPS_DIR / f"scene-{scene_num:02d}-kenburns.mp4"
        source = animated if animated.exists() else kenburns if kenburns.exists() else None

        if source is None:
            print(f"  [scene-{scene_num:02d}] WARNING: no clip found, skipping")
            continue

        output = norm_dir / f"scene-{scene_num:02d}.mp4"
        if output.exists():
            print(f"  [scene-{scene_num:02d}] SKIP — normalized already exists")
            continue

        cmd = [
            FFMPEG, "-y", "-i", str(source),
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-pix_fmt", "yuv420p",
            "-an",  # strip audio from individual clips
            str(output)
        ]
        _run_ffmpeg(cmd, f"normalize scene-{scene_num:02d}")

    return norm_dir


# ---------------------------------------------------------------------------
# Composite final video
# ---------------------------------------------------------------------------

def composite_video(dry_run: bool = False):
    """Concatenate all 19 clips and add audio."""
    print("\n=== Compositing final video ===")

    # Normalize clips first
    norm_dir = normalize_clips()

    # Build concat list
    concat_list = norm_dir / "concat.txt"
    lines = []
    missing = []
    for scene_num in range(1, 20):
        clip = norm_dir / f"scene-{scene_num:02d}.mp4"
        if clip.exists():
            lines.append(f"file '{clip.name}'")
        else:
            missing.append(scene_num)
            print(f"  WARNING: scene-{scene_num:02d} missing from normalized clips")

    if missing:
        print(f"\n  Missing scenes: {missing}")
        print("  Proceeding with available clips...")

    with open(concat_list, "w") as f:
        f.write("\n".join(lines))

    # Concatenate video (no audio)
    video_no_audio = FINAL_DIR / "video-sin-audio.mp4"
    cmd = [
        FFMPEG, "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(video_no_audio)
    ]
    _run_ffmpeg(cmd, "concatenate all clips")
    print(f"  Video without audio: {video_no_audio}")

    # --- Matthew version ---
    narration_matthew = AUDIO_DIR / "narration-full.mp3"
    bg_music = AUDIO_DIR / "bg-music" / "i-walk-with-ghosts-scott-buckley.mp3"
    matthew_output = FINAL_DIR / "mushin-pax-matthew.mp4"

    if narration_matthew.exists() and bg_music.exists():
        print("\n  Compositing Matthew version...")
        cmd = [
            FFMPEG, "-y",
            "-i", str(video_no_audio),
            "-i", str(narration_matthew),
            "-i", str(bg_music),
            "-filter_complex",
            "[1:a]volume=1.0[voice];[2:a]volume=0.15[music];[voice][music]amix=inputs=2:duration=first[aout]",
            "-map", "0:v", "-map", "[aout]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(matthew_output)
        ]
        _run_ffmpeg(cmd, "composite Matthew version with audio")
        size_mb = matthew_output.stat().st_size / (1024 * 1024)
        print(f"  Matthew version: {matthew_output} ({size_mb:.1f} MB)")
    else:
        print("  WARNING: Matthew narration or bg music not found, skipping")

    # --- Myrrdin version (partial, 3/5 parts) ---
    narration_myrrdin = AUDIO_MYRRDIN_DIR / "narration-full.mp3"
    myrrdin_output = FINAL_DIR / "mushin-pax-myrrdin.mp4"

    if narration_myrrdin.exists() and bg_music.exists():
        print("\n  Compositing Myrrdin version (partial)...")
        cmd = [
            FFMPEG, "-y",
            "-i", str(video_no_audio),
            "-i", str(narration_myrrdin),
            "-i", str(bg_music),
            "-filter_complex",
            "[1:a]volume=1.0[voice];[2:a]volume=0.15[music];[voice][music]amix=inputs=2:duration=first[aout]",
            "-map", "0:v", "-map", "[aout]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            str(myrrdin_output)
        ]
        _run_ffmpeg(cmd, "composite Myrrdin version with audio")
        size_mb = myrrdin_output.stat().st_size / (1024 * 1024)
        print(f"  Myrrdin version: {myrrdin_output} ({size_mb:.1f} MB)")
    else:
        print("  WARNING: Myrrdin narration not found, skipping")

    return {
        "video_no_audio": str(video_no_audio),
        "matthew": str(matthew_output) if matthew_output.exists() else None,
        "myrrdin": str(myrrdin_output) if myrrdin_output.exists() else None,
        "missing_scenes": missing,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

async def main():
    parser = argparse.ArgumentParser(description="Produce the Mushin Pax 9-minute video")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    parser.add_argument("--animated", action="store_true", help="Generate animated clips only (Kling v2.6)")
    parser.add_argument("--kenburns", action="store_true", help="Generate Ken Burns clips only (ffmpeg)")
    parser.add_argument("--composite", action="store_true", help="Composite final video only")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without executing")
    args = parser.parse_args()

    if not any([args.all, args.animated, args.kenburns, args.composite]):
        parser.print_help()
        return

    # Ensure output directories exist
    CLIPS_DIR.mkdir(exist_ok=True)
    FINAL_DIR.mkdir(exist_ok=True)

    results = {"animated": [], "kenburns": [], "composite": {}}

    # --- Ken Burns (free, do first) ---
    if args.all or args.kenburns:
        print("\n" + "=" * 60)
        print("PHASE 1: Ken Burns clips (ffmpeg, free)")
        print("=" * 60)
        results["kenburns"] = generate_kenburns_clips(dry_run=args.dry_run)

    # --- Animated (costs money) ---
    if args.all or args.animated:
        print("\n" + "=" * 60)
        print("PHASE 2: Animated clips (Kling v2.6, ~$2.45 USD)")
        print("=" * 60)
        if not args.dry_run:
            print("  Starting Kling v2.6 generation via Replicate API...")
        results["animated"] = await generate_animated_clips(dry_run=args.dry_run)

    # --- Composite ---
    if args.all or args.composite:
        if args.dry_run:
            print("\n[DRY RUN] Would composite 19 clips + audio into final videos")
        else:
            print("\n" + "=" * 60)
            print("PHASE 3: Composite final video")
            print("=" * 60)
            results["composite"] = composite_video(dry_run=args.dry_run)

    # --- Summary ---
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    kb_ok = sum(1 for r in results["kenburns"] if r.get("status") == "ok")
    kb_skip = sum(1 for r in results["kenburns"] if r.get("status") == "skipped")
    anim_ok = sum(1 for r in results["animated"] if r.get("status") == "ok")
    anim_skip = sum(1 for r in results["animated"] if r.get("status") == "skipped")
    anim_err = sum(1 for r in results["animated"] if r.get("status") == "error")
    anim_cost = sum(r.get("cost", 0) for r in results["animated"] if r.get("status") in ("ok", "dry_run"))

    print(f"  Ken Burns: {kb_ok} generated, {kb_skip} skipped")
    print(f"  Animated:  {anim_ok} generated, {anim_skip} skipped, {anim_err} errors")
    print(f"  Est. cost: ${anim_cost:.2f} USD")

    if results.get("composite"):
        comp = results["composite"]
        if comp.get("matthew"):
            size = os.path.getsize(comp["matthew"]) / (1024 * 1024)
            print(f"  Matthew:   {comp['matthew']} ({size:.1f} MB)")
        if comp.get("myrrdin"):
            size = os.path.getsize(comp["myrrdin"]) / (1024 * 1024)
            print(f"  Myrrdin:   {comp['myrrdin']} ({size:.1f} MB)")
        if comp.get("missing_scenes"):
            print(f"  Missing:   scenes {comp['missing_scenes']}")

    # Save results log
    log_path = FINAL_DIR / "production_log.json"
    with open(log_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Log saved: {log_path}")


if __name__ == "__main__":
    asyncio.run(main())
