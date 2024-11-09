import random

from moviepy.editor import VideoFileClip
from pathlib import Path

# Feel free to modify these to suit your needs
DEFAULT_INPUT_DIR = "../data/train_sample_videos/"
DEFAULT_OUTPUT_DIR = "../data/compressed"

def compress_video(input_dir, output_dir, video):
    """
    This function compresses .mp4's using the moviepy module.

    TODO:
    Multiprocessing later down the line, for obvious reasons.
    Additionally, we can look into the ffmpeg library, which is typically
    the more flexible module for this kind of job.
    """

    # If the output folder doesn't exist, make it.
    # Note that the input folder MUST exist, as it contains the video.
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    input_path = f"{input_dir}/{video}"
    output_path = f"{output_dir}/{video}"

    # Choose between fast and ultrafast presets. This yields lower quality, but faster videos.
    compression_level = random.choice(["fast", "ultrafast"])

    video_clip = VideoFileClip(input_path)
    video_clip.write_videofile(
        output_path,
        codec="libx264",  # Use H.264 video codec
        preset=compression_level,
        audio=False # I assume we won't be needing audio?
    )

