# FolderDiff

FolderDiff is a Python script that compares the contents of two folders and outputs the unique file names that are not present in both folders. The comparison ignores file extensions, so files with the same name but different extensions will not be considered different. The unique file names are output to a text file in alphabetical order, with the file name containing the current date and time, along with the names of the two folders being compared.

After the comparison, the script offers the option to delete duplicates in either folder.

## Requirements
- Python 3.6 or higher

## Usage
1. Clone or download the repository to your local machine.
2. Open a terminal/command prompt and navigate to the folder containing the script.
3. Run the script using the command python folder_diff.py.
4. When prompted, enter the paths of the two folders you want to compare, starting from the root directory.
5. The script will generate a text file with the unique file names in alphabetical order. The file will be named in the format YYYYMMDD_HHMMSS_folder1name_folder2name.txt and will be located in the same directory as the script.
6. The script will then ask if you want to delete duplicates in one of the folders. If you choose to do so, it will prompt you to select which folder to delete duplicates from and print the deleted file paths to the console.

## Example
```
$ python folder_diff.py
Enter the path of the first folder (from root): /path/to/folder1
Enter the path of the second folder (from root): /path/to/folder2
Comparison results have been written to 20230411_154527_folder1_folder2.txt
Do you want to delete the duplicates in one folder? [y/N]: y
Enter 1 to delete duplicates in the first folder (/path/to/folder1), 2 for the second folder (/path/to/folder2), or 3 to exit: 1
Deleted: /path/to/folder1/somefile.txt
Deleted: /path/to/folder1/anotherfile.doc
```