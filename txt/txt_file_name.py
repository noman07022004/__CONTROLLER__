import tkinter as tk
from tkinter import filedialog
import os

# Function to select multiple text files


def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    files = filedialog.askopenfilenames(
        title="Select text files", filetypes=[("Text files", "*.txt")])
    return files

# Function to select the directory to save the output file


def select_output_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title="Select output directory")
    return directory

# Main function to create the output file with file names


def create_output_file():
    # Step 1: Select multiple text files
    files = select_files()
    if not files:
        print("No files selected.")
        return

    # Step 2: Ask where to save the output file
    output_directory = select_output_directory()
    if not output_directory:
        print("No output directory selected.")
        return

    # Step 3: Define the output file name
    output_file_path = os.path.join(output_directory, "__file_name__.txt")

    # Step 4: Write the selected file names into the output file
    with open(output_file_path, "w") as output_file:
        for file in files:
            file_name = os.path.basename(file)  # Extract just the file name
            output_file.write(file_name + "\n")

    print(f"Output file created at: {output_file_path}")


# Run the main function
if __name__ == "__main__":
    create_output_file()
