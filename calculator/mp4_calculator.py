import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog


def get_video_details(filenames):
    total_duration = 0  # in seconds
    total_size = 0  # in bytes

    for file in filenames:
        try:
            # Get file size in bytes
            file_size = os.path.getsize(file)
            total_size += file_size

            # Get video duration in seconds
            video = VideoFileClip(file)
            duration = video.duration
            total_duration += duration

            # Close the video file to release resources
            video.reader.close()
            video.audio.reader.close_proc()
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    # Convert size to MB and GB
    total_size_mb = total_size / (1024 * 1024)
    total_size_gb = total_size / (1024 * 1024 * 1024)

    # Convert duration to minutes and hours
    total_duration_minutes = total_duration / 60
    total_duration_hours = total_duration / 3600

    return total_duration_minutes, total_duration_hours, total_size_mb, total_size_gb


def main():
    # Hide the root tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open file dialog and allow multiple selection
    filenames = filedialog.askopenfilenames(
        title="Select MP4 files",
        filetypes=[("MP4 files", "*.mp4")]
    )

    if filenames:
        # Calculate video details
        total_duration_minutes, total_duration_hours, total_size_mb, total_size_gb = get_video_details(
            filenames)

        # Display results with 2 decimal places
        result_text = (
            f"Total duration: {total_duration_minutes:.2f} minutes ({
                total_duration_hours:.2f} hours)\n"
            f"Total size: {total_size_mb:.2f} MB ({total_size_gb:.2f} GB)"
        )
        print(result_text)
    else:
        print("No files selected.")


if __name__ == "__main__":
    main()
