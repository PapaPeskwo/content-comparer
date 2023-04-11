import os
from pathlib import Path

def get_filenames_without_extension(folder_path):
    filenames = set()
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_without_ext = os.path.splitext(file)[0]
            filenames.add(file_without_ext)
    return filenames

def main():
    folder1_path = input("Enter the path of the first folder (from root):\n")
    folder2_path = input("Enter the path of the second folder (from root):\n")

    folder1_files = get_filenames_without_extension(folder1_path)
    folder2_files = get_filenames_without_extension(folder2_path)

    unique_files = folder1_files.symmetric_difference(folder2_files)
    sorted_unique_files = sorted(unique_files)

    folder1_name = os.path.basename(os.path.normpath(folder1_path))
    folder2_name = os.path.basename(os.path.normpath(folder2_path))
    output_filename = f"{folder1_name}_{folder2_name}.txt"

    with open(output_filename, "w") as output_file:
        for unique_file in sorted_unique_files:
            output_file.write(f"{unique_file}\n")

    print(f"Comparison results have been written to {output_filename}")

if __name__ == "__main__":
    main()
