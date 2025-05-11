# import os
# import time
# import shutil
# from datetime import datetime
# import tkinter as tk
# from gui import DownloadOrganizerGUI

# # ========================== CONFIG ==========================
# SOURCE_CODE_EXTENSIONS = ['py', 'java', 'cpp', 'js', 'html', 'css', 'php', 'rb']

# EXTENSION_MAP = {
#     "Images": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
#     "Videos": ["mp4", "mov", "avi", "mkv", "webm"],
#     "Documents": ["pdf", "docx", "doc", "txt", "pptx", "xlsx", "csv", "odt"],
#     "Audio": ["mp3", "wav", "aac", "flac"],
#     "Archives": ["zip", "rar", "7z", "tar", "gz"],
#     "Executables": ["exe", "msi", "apk"],
#     "Scripts": ["py", "js", "sh", "bat", "rb"],
#     "Others": []
# }

# # ========================== FILE UTILS ==========================
# def get_file_category(file_extension):
#     for category, extensions in EXTENSION_MAP.items():
#         if file_extension.lower() in extensions:
#             return category
#     return "Miscellaneous"

# def get_creation_date(file_path):
#     creation_time = os.path.getctime(file_path)
#     return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

# def create_directory(path):
#     if not os.path.exists(path):
#         os.makedirs(path)

# def move_file(src_path, dest_path):
#     try:
#         dest_dir = os.path.dirname(dest_path)
#         create_directory(dest_dir)

#         if os.path.exists(dest_path):
#             base, extension = os.path.splitext(dest_path)
#             counter = 1
#             while os.path.exists(f"{base} ({counter}){extension}"):
#                 counter += 1
#             dest_path = f"{base} ({counter}){extension}"

#         shutil.move(src_path, dest_path)
#         print(f"[DEBUG] Moved: {src_path} -> {dest_path}")
#         return True
#     except Exception as e:
#         print(f"[ERROR] Failed to move {src_path}: {e}")
#         return False

# # ========================== SORTING LOGIC ==========================
# def organize_files(folder_path):
#     files_to_process = [
#         f for f in os.listdir(folder_path) 
#         if os.path.isfile(os.path.join(folder_path, f)) and not f.endswith(tuple(SOURCE_CODE_EXTENSIONS))
#     ]

#     for file in files_to_process:
#         file_path = os.path.join(folder_path, file)
#         file_extension = file.split('.')[-1]
#         category = get_file_category(file_extension)
#         creation_date = get_creation_date(file_path)
#         dest_dir = os.path.join(folder_path, category, file_extension, creation_date)
#         dest_file = os.path.join(dest_dir, file)
#         move_file(file_path, dest_file)

#     return len(files_to_process)

# def get_total_files_in_folder(folder_path):
#     return len([
#         f for f in os.listdir(folder_path)
#         if os.path.isfile(os.path.join(folder_path, f)) and not f.endswith(tuple(SOURCE_CODE_EXTENSIONS))
#     ])

# # ========================== MAIN LOGIC ==========================
# def organize_folder(folder_path, gui=None):
#     try:
#         print(f"\n[INFO] Starting organization for: {folder_path}")

#         total_files = get_total_files_in_folder(folder_path)
#         print(f"[INFO] Total files to process: {total_files}")

#         if total_files == 0:
#             print("[INFO] No files to process.")
#             if gui:
#                 gui.set_progress(0, 1)
#                 gui.show_summary(0, 0, 0.0)
#             return

#         start_time = time.time()
#         moved = organize_files(folder_path)

#         if gui:
#             gui.set_progress(total_files, total_files)
#             gui.show_summary(moved, 0, time.time() - start_time)

#         print(f"[INFO] Done. Moved {moved} files in {time.time() - start_time:.2f} seconds.\n")

#     except Exception as e:
#         print(f"[ERROR] Exception occurred while organizing: {e}")
#         if gui:
#             gui.status_label.config(text=f"Error: {e}")

# def create_app_window():
#     window = tk.Tk()

#     def on_start(folder_path):
#         organize_folder(folder_path, gui)

#     gui = DownloadOrganizerGUI(window, on_start)
#     window.mainloop()

# if __name__ == "__main__":
#     create_app_window()




















import os
import time
import shutil
from datetime import datetime
import tkinter as tk
from gui import DownloadOrganizerGUI

# ========================== CONFIG ==========================
SOURCE_CODE_EXTENSIONS = ['py', 'java', 'cpp', 'js', 'html', 'css', 'php', 'rb']

EXTENSION_MAP = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "svg"],
    "Videos": ["mp4", "mov", "avi", "mkv", "webm"],
    "Documents": ["pdf", "docx", "doc", "txt", "pptx", "xlsx", "csv", "odt"],
    "Audio": ["mp3", "wav", "aac", "flac"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"],
    "Executables": ["exe", "msi", "apk"],
    "Scripts": ["py", "js", "sh", "bat", "rb"],
    "Others": []
}

# ========================== FILE UTILS ==========================
def get_file_category(file_extension):
    for category, extensions in EXTENSION_MAP.items():
        if file_extension.lower() in extensions:
            return category
    return "Miscellaneous"

def get_creation_date(file_path):
    creation_time = os.path.getctime(file_path)
    return datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_file(src_path, dest_path):
    try:
        dest_dir = os.path.dirname(dest_path)
        create_directory(dest_dir)

        if os.path.exists(dest_path):
            base, extension = os.path.splitext(dest_path)
            counter = 1
            while os.path.exists(f"{base} ({counter}){extension}"):
                counter += 1
            dest_path = f"{base} ({counter}){extension}"

        shutil.move(src_path, dest_path)
        print(f"[DEBUG] Moved: {src_path} -> {dest_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to move {src_path}: {e}")
        return False

# ========================== SORTING LOGIC ==========================
def organize_files(folder_path):
    # Create a parent 'sorted' directory if it doesn't exist
    sorted_folder = os.path.join(folder_path, "sorted")
    create_directory(sorted_folder)

    files_to_process = [
        f for f in os.listdir(folder_path) 
        if os.path.isfile(os.path.join(folder_path, f)) and not f.endswith(tuple(SOURCE_CODE_EXTENSIONS))
    ]

    for file in files_to_process:
        file_path = os.path.join(folder_path, file)
        file_extension = file.split('.')[-1]
        category = get_file_category(file_extension)
        creation_date = get_creation_date(file_path)

        # Build the destination directory inside 'sorted'
        dest_dir = os.path.join(sorted_folder, category, file_extension, creation_date)
        create_directory(dest_dir)

        dest_file = os.path.join(dest_dir, file)
        move_file(file_path, dest_file)

    return len(files_to_process)

def get_total_files_in_folder(folder_path):
    return len([
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.endswith(tuple(SOURCE_CODE_EXTENSIONS))
    ])

# ========================== MAIN LOGIC ==========================
def organize_folder(folder_path, gui=None):
    try:
        print(f"\n[INFO] Starting organization for: {folder_path}")

        total_files = get_total_files_in_folder(folder_path)
        print(f"[INFO] Total files to process: {total_files}")

        if total_files == 0:
            print("[INFO] No files to process.")
            if gui:
                gui.set_progress(0, 1)
                gui.show_summary(0, 0, 0.0)
            return

        start_time = time.time()
        moved = organize_files(folder_path)

        if gui:
            gui.set_progress(total_files, total_files)
            gui.show_summary(moved, 0, time.time() - start_time)

        print(f"[INFO] Done. Moved {moved} files in {time.time() - start_time:.2f} seconds.\n")

    except Exception as e:
        print(f"[ERROR] Exception occurred while organizing: {e}")
        if gui:
            gui.status_label.config(text=f"Error: {e}")

def create_app_window():
    window = tk.Tk()

    def on_start(folder_path):
        organize_folder(folder_path, gui)

    gui = DownloadOrganizerGUI(window, on_start)
    window.mainloop()

if __name__ == "__main__":
    create_app_window()
