import os
import tkinter as tk
from tkinter import filedialog

def get_file_paths():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    files = filedialog.askopenfilenames(
        initialdir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        title="Select one or more text files",
        filetypes=(("Text files", "*.txt"),)
    )
    return root.tk.splitlist(files)

def calculate_length_and_words(file_paths):
    total_characters = 0
    total_words = 0
    
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            total_characters += len(content)
            total_words += len(content.split())
    return total_characters, total_words

def main():
    file_paths = get_file_paths()
    if not file_paths:
        print("No files selected.")
        return

    total_characters, total_words = calculate_length_and_words(file_paths)
    
    print(f"Total characters: {total_characters}")
    print(f"Total words: {total_words}")
    print(f"Characters/Words: {round(total_characters/total_words,2)}")

if __name__ == "__main__":
    main()
