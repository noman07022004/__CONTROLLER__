import tkinter as tk
from tkinter import filedialog
import os


def main():
    # Initialize Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask user to select multiple text files
    input_files = filedialog.askopenfilenames(
        title="Select TXT Files",
        filetypes=[("Text Files", "*.txt")],
        defaultextension=".txt"
    )

    if not input_files:
        print("No files selected.")
        return

    # Ask user for the directory to save the output file
    output_dir = filedialog.askdirectory(title="Select Output Directory")

    if not output_dir:
        print("No output directory selected.")
        return

    # Define the name of the output file
    output_file_path = os.path.join(output_dir, "__path__.txt")

    # Write the paths of the selected files into the output file
    try:
        with open(output_file_path, 'w') as output_file:
            for file_path in input_files:
                output_file.write(f"{file_path}\n")
        print(f"Paths successfully written to {output_file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    main()
