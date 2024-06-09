import os
import tkinter as tk
from tkinter import filedialog


def combine_files(files, num_files, output_dir):
    for i in range(0, len(files), num_files):
        start = i + 1
        end = min(i + num_files, len(files))
        with open(
            os.path.join(output_dir, f"{start//num_files+1}.txt"), "w", encoding="utf-8"
        ) as outfile:
            for j in range(i, end):
                with open(files[j], "rb") as infile:
                    content = infile.read().decode("utf-8", errors="ignore")
                    outfile.write(content)
                outfile.write("\n")  # Add a newline after each file's content

        print(f"Combined files {start//num_files+1}.")


def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        filetypes=[("Text files", "*.txt")])
    file_paths = sorted(
        file_paths, key=lambda x: int(os.path.splitext(os.path.basename(x))[0])
    )
    output_dir = filedialog.askdirectory(
        initialdir=os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))
        )
    )
    num_files = int(input("Enter the number of files to combine at a time: "))
    combine_files(file_paths, num_files, output_dir)


if __name__ == "__main__":
    select_files()
