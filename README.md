# Automated File Organizer Utility
![Image](https://github.com/user-attachments/assets/f6c0117e-896d-4d91-9931-acafb11b5601)
## Project Description

The **Automated File Organizer Utility** is a Python-based solution designed to simplify file management by automatically sorting files into appropriate categories based on their extensions and creation dates. This tool offers a streamlined approach to organizing downloads or any folder containing a mix of files into a more structured format. The project utilizes a modular architecture to keep the logic clean and maintainable, with features that include file categorization, directory creation, and conflict resolution in file movement.

## Problem Statement

With the increasing amount of data and files stored on local systems, managing files can quickly become chaotic. The need for an automatic and efficient way to organize files based on their types (e.g., images, videos, documents) and metadata (e.g., creation date) has become more evident. Manual sorting can be time-consuming, error-prone, and tedious, especially when dealing with a large volume of files. This project was developed to tackle this problem by automatically sorting files into categorized directories with minimal user intervention.

## Objective

The primary objective of the **Automated File Organizer Utility** is to automate the process of organizing files stored in a specific folder. The key goals of the project include:

1. **Automatic File Categorization**: Sort files based on their extensions (e.g., images, documents, videos) into respective subfolders.
2. **Creation Date Sorting**: Files will be sorted not only by type but also by the creation date, ensuring that older files are grouped together.
3. **Conflict Resolution**: Handle cases where a file with the same name already exists in the destination folder by renaming the file to avoid overwriting.
4. **User Interface**: A simple and intuitive graphical user interface (GUI) built using Tkinter that allows users to select the folder to be organized and monitor the progress.

## Key Features

* **File Categorization**: Automatically categorizes files into predefined folders such as "Images", "Videos", "Documents", "Audio", etc., based on their extensions.
* **Creation Date Sorting**: Files are not just sorted by type; they are further organized into subfolders based on their creation date, ensuring better chronological organization.
* **Conflict Resolution**: In case of name conflicts, the utility renames files by appending a counter (e.g., `file (1).jpg`, `file (2).jpg`) to avoid overwriting existing files.
* **Progress Tracking**: The utility provides progress feedback to the user through the GUI, including the number of files moved and the time taken.
* **Cross-Platform Support**: The tool is built using Python, making it compatible with multiple platforms (Windows, Linux, macOS).

## Logical Workflow / Algorithm

The algorithm behind the **Automated File Organizer Utility** follows a simple and efficient structure:

1. **Initialize the GUI**: The user interacts with a Tkinter-based GUI where they select the folder to be organized.
2. **Count Files**: The program first checks the total number of files in the selected folder, excluding source code files (e.g., `.py`, `.html`).
3. **Create Parent Folder**: A parent folder named "sorted" is created (if it doesn’t exist) in the selected directory.
4. **Categorize Files**: For each file:

   * Determine its file extension.
   * Identify the category (e.g., Images, Videos, Documents) based on the file extension using a predefined dictionary.
   * Determine the file's creation date.
5. **Move Files**: Each file is moved into its respective category folder under the "sorted" folder, further organized by its creation date.
6. **Handle Conflicts**: If a file with the same name already exists in the target folder, the program appends a counter to the filename to avoid overwriting.
7. **Progress Feedback**: The progress of the file sorting operation is updated on the GUI, and the final summary is displayed once the process is complete.

## Technology Stack

* **Python**: The core programming language used for building the application.
* **Tkinter**: A built-in Python library for creating graphical user interfaces (GUIs).
* **Shutil**: Python library used for file manipulation (moving files).
* **OS**: Python’s OS module is used to interact with the file system (e.g., checking file existence, creating directories).
* **Datetime**: Python module used to retrieve the creation date of files.
* **Config File**: Used to store file extensions mapping and other configuration settings (e.g., file categories, excluded extensions).

## Code Explanation (Line by Line)

1. **Imports**:

   ```python
   import os
   import time
   import shutil
   from datetime import datetime
   import tkinter as tk
   from gui import DownloadOrganizerGUI
   ```

   These are the necessary Python libraries for file manipulation, time tracking, GUI creation, and datetime handling.

2. **Configuration Variables**:
   The `SOURCE_CODE_EXTENSIONS` and `EXTENSION_MAP` dictionaries define which file extensions belong to which categories. This helps in categorizing files correctly.

3. **Helper Functions**:

   * `get_file_category(file_extension)`: Determines the category of a file based on its extension.
   * `get_creation_date(file_path)`: Returns the creation date of a file in `YYYY-MM-DD` format.
   * `create_directory(path)`: Ensures that a directory exists at the given path; if not, it creates it.
   * `move_file(src_path, dest_path)`: Moves a file from the source path to the destination path, ensuring that the destination directory exists.

4. **Main Sorting Function**:
   The `organize_files(folder_path)` function handles the actual file organization. It iterates over all files, categorizes them, creates necessary subdirectories under the `sorted` folder, and moves files into the appropriate folder.

5. **GUI Interaction**:

   * The GUI is initialized in the `create_app_window()` function.
   * The user selects the folder, and upon clicking start, the `on_start()` function is triggered to organize the files.
   * The progress is tracked and displayed through the GUI.

6. **Execution Block**:
   The `if __name__ == "__main__":` block ensures that the script runs the GUI when executed directly.

## Output

After the utility runs successfully, the output will be:

1. **Organized Folder Structure**: The files are neatly organized into the "sorted" folder, where each category (e.g., "Images", "Videos") has subfolders based on file extensions and creation dates.

2. **Progress Summary**: The GUI will display a summary of the number of files moved, the number of skipped files, and the total time taken to organize the files.

Example output on the console:

```
[INFO] Starting organization for: C:\Users\YourUser\Downloads
[INFO] Total files to process: 50
[INFO] Moved 45 files in 10.24 seconds.
```
