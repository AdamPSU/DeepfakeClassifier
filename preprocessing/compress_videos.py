import random
import logging
from moviepy.editor import VideoFileClip
from pathlib import Path

# Set the logging level to ERROR to suppress MoviePy's INFO and DEBUG messages
logging.getLogger("moviepy").setLevel(logging.CRITICAL)

# Feel free to modify these to suit your needs
DEFAULT_INPUT_DIR = Path("../data/train_sample_videos/")
DEFAULT_OUTPUT_DIR = Path("../data/compressed")

def compress_video(input_path, output_dir):
    """
    This function compresses .mp4's using the moviepy module.

    TODO:
    Multiprocessing later down the line, for obvious reasons.
    Additionally, we can look into the ffmpeg library, which is typically
    the more flexible module for this kind of job.
    """

    # If the output folder doesn't exist, make it.
    # Note that the input folder MUST exist, as it contains the video.
    output_dir.mkdir(parents=True, exist_ok=True)

    video_name = input_path.name
    output_path = output_dir / video_name # Add video to the output folder

    # Convert from Path objects to Python strings
    input_as_string = input_path.as_posix()
    output_as_string = output_path.as_posix()

    # Choose between fast and ultrafast presets. This yields lower quality, but faster videos.
    compression_level = random.choice(["fast", "ultrafast"])

    video_clip = VideoFileClip(input_as_string)
    video_clip.write_videofile(
        output_as_string,
        codec="libx264",  # Use H.264 video codec for compression
        preset=compression_level,
        audio=False # I assume we won't be needing audio?
    )

# TODO: this entire thing should be multi-processed
if __name__ == '__main__':
    # Get all videos in input directory by matching all .mp4 files with glob.
    all_videos = DEFAULT_INPUT_DIR.glob("*.mp4")

    for video_path in all_videos:
        compress_video(video_path, DEFAULT_OUTPUT_DIR)
