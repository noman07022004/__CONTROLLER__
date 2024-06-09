import os
import tkinter as tk
from tkinter import filedialog

# Function to create a directory if it doesn't exist


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to create a file if it doesn't exist


def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w', encoding="utf-8") as f:
            f.close()

# Function to select a directory using a GUI


def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    current_directory = os.getcwd()
    folder_selected = filedialog.askdirectory(initialdir=current_directory)
    return folder_selected


# Ask the user to select the base directory
base_dir = select_directory()
if not base_dir:
    print("No directory selected, exiting the script.")
    exit()

# Ask the user for the project name
project_name = input("Please enter the project name: ")
project_dir = os.path.join(base_dir, project_name)

# Create the project directory and subdirectories
create_dir(project_dir)

# Create the 'text' folder
text_dir = os.path.join(project_dir, 'text')
create_dir(text_dir)

# Create the 'unformatted', 'combined_unformatted' folder and '0.txt' file inside 'text'
unformatted_dir = os.path.join(text_dir, 'unformatted')
create_dir(unformatted_dir)
combined_unformatted_dir = os.path.join(text_dir, 'combined_unformatted')
create_dir(combined_unformatted_dir)
create_file(os.path.join(unformatted_dir, '0.txt'))

# Create 'Audio', 'Video', 'Captions', and 'Thumbnail' folders
audio_dir = os.path.join(project_dir, 'audio')
video_dir = os.path.join(project_dir, 'video')
captions_dir = os.path.join(project_dir, 'captions')

create_dir(audio_dir)
create_dir(video_dir)
create_dir(captions_dir)


# Create the 'unformatted' folder inside 'Captions'
create_dir(os.path.join(captions_dir, 'unformatted'))

# Create 'Others' folder with 'title.txt' and 'description.txt' files
others_dir = os.path.join(project_dir, 'others')
create_dir(others_dir)
create_file(os.path.join(others_dir, 'title.txt'))
create_file(os.path.join(others_dir, 'description.txt'))


thumbnail_dir = os.path.join(others_dir, 'thumbnail')
create_dir(thumbnail_dir)


print(f"Project '{project_name}' has been created successfully at '{
      base_dir}'!")
