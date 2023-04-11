import os
from pathlib import Path
from datetime import datetime

def get_filenames_without_extension(folder_path):
    filenames = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_without_ext = os.path.splitext(file)[0]
            full_path = os.path.join(root, file)
            filenames[file_without_ext] = full_path
    return filenames

def delete_duplicates(folder_path, duplicates):
    for file, full_path in duplicates.items():
        file_path = os.path.join(folder_path, full_path)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

def main():
    folder1_path = input("Enter the path of the first folder (from root):\n")
    folder2_path = input("Enter the path of the second folder (from root):\n")

    folder1_files = get_filenames_without_extension(folder1_path)
    folder2_files = get_filenames_without_extension(folder2_path)

    unique_files = set(folder1_files.keys()).symmetric_difference(set(folder2_files.keys()))
    duplicates = set(folder1_files.keys()).intersection(set(folder2_files.keys()))

    sorted_unique_files = sorted(unique_files)
    sorted_duplicates = sorted(duplicates)

    folder1_name = os.path.basename(os.path.normpath(folder1_path))
    folder2_name = os.path.basename(os.path.normpath(folder2_path))
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{current_time}_{folder1_name}_{folder2_name}.txt"

    with open(output_filename, "w") as output_file:
        output_file.write("--Duplicates--\n")
        for duplicate in sorted_duplicates:
            output_file.write(f"{duplicate}\n")
        
        output_file.write("\n--Unique Files--\n")
        for unique_file in sorted_unique_files:
            output_file.write(f"{unique_file}\n")

    print(f"Comparison results have been written to {output_filename}")

    if duplicates:
        delete_choice = input("Do you want to delete the duplicates in one folder? [y/N]: ")
        if delete_choice.lower() == 'y':
            while True:
                folder_choice = input(f"Enter 1 to delete duplicates in the first folder \n({folder1_path}) \n\nEnter 2 to delete duplicates in the second folder \n({folder2_path}) \n\nEnter 3 to exit\n ")
                if folder_choice == '1':
                    duplicates = {k: v for k, v in folder1_files.items() if k not in unique_files}
                    delete_duplicates(folder1_path, duplicates)
                    break
                elif folder_choice == '2':
                    duplicates = {k: v for k, v in folder2_files.items() if k not in unique_files}
                    delete_duplicates(folder2_path, duplicates)
                    break
                elif folder_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    main()
