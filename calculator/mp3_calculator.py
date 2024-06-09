import os
import tkinter as tk
from tkinter import filedialog
from mutagen.mp3 import MP3

def select_files():
    root = tk.Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(filetypes=[("MP3 files", "*.mp3")])
    return file_paths

def calculate_total_length_and_size(file_paths):
    total_length_seconds = 0
    total_size_bytes = 0

    for file_path in file_paths:
        audio = MP3(file_path)
        total_length_seconds += audio.info.length
        total_size_bytes += os.path.getsize(file_path)

    total_length_minutes = total_length_seconds / 60
    total_length_hours = total_length_minutes / 60

    total_size_MB = total_size_bytes / (1024 * 1024)
    total_size_GB = total_size_MB / 1024

    return total_length_minutes, total_length_hours, total_size_MB, total_size_GB

def main():
    file_paths = select_files()
    total_length_minutes, total_length_hours, total_size_MB, total_size_GB = calculate_total_length_and_size(file_paths)

    print(f"Total length: {format(total_length_minutes, '.2f')} minutes ({format(total_length_hours, '.2f')} hours)")
    print(f"Total size: {format(total_size_MB, '.2f')} MB ({format(total_size_GB, '.2f')} GB)")

if __name__ == "__main__":
    main()
