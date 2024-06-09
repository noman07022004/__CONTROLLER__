import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog

def get_file_size(file_path):
    size_in_bytes = os.path.getsize(file_path)
    size_in_mb = size_in_bytes / (1024 * 1024)
    size_in_gb = size_in_bytes / (1024 * 1024 * 1024)
    return size_in_mb, size_in_gb

def get_video_length(file_path):
    clip = VideoFileClip(file_path)
    duration_in_sec = clip.duration
    duration_in_min = duration_in_sec / 60
    duration_in_hour = duration_in_sec / 3600
    return duration_in_min, duration_in_hour

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(filetypes=[("MP4 files", "*.mp4")])
    total_duration_min = 0
    total_duration_hour = 0
    total_size_mb = 0
    total_size_gb = 0

    for file_path in file_paths:
        duration_min, duration_hour = get_video_length(file_path)
        size_mb, size_gb = get_file_size(file_path)
        total_duration_min += duration_min
        total_duration_hour += duration_hour
        total_size_mb += size_mb
        total_size_gb += size_gb

    print(f"Total duration: {total_duration_min:.2f} minutes ({total_duration_hour:.2f} hours)")
    print(f"Total size: {total_size_mb:.2f} MB ({total_size_gb:.2f} GB)")

if __name__ == "__main__":
    main()
