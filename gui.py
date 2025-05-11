# import tkinter as tk
# from tkinter import ttk, filedialog
# from PIL import Image, ImageTk, ImageSequence

# class DownloadOrganizerGUI:
#     def __init__(self, root, start_callback):
#         self.root = root
#         self.root.title("Automated Download Organizer")
#         self.root.attributes('-fullscreen', True)
#         self.start_callback = start_callback
#         self.selected_path = tk.StringVar()

#         # --- Canvas for GIF background & controls
#         self.canvas = tk.Canvas(root, highlightthickness=0)
#         self.canvas.pack(fill="both", expand=True)
#         root.bind("<Escape>", lambda e: root.destroy())
#         root.bind("<Configure>", self.on_resize)

#         # --- Load GIF frames
#         self.gif_path = r"background.gif"
#         self.original_gif = Image.open(self.gif_path)
#         self.frames = []
#         self._widgets = {}
#         self.path_label = None
#         self.progress = None
#         self.status_label = None

#         # Delay initialization
#         self.root.after(100, self.initial_setup)

#     def initial_setup(self):
#         # Wait until window is fully rendered to initialize GIF
#         self.root.update_idletasks()
#         w, h = self.canvas.winfo_width(), self.canvas.winfo_height()

#         if w < 100 or h < 100:
#             self.root.after(100, self.initial_setup)
#             return

#         self.prepare_frames(w, h)
#         self.animate(0)
#         self.build_controls()  # Ensure controls are created after setup
#         self.reposition_controls()  # Now it will work as expected

#     def prepare_frames(self, width, height):
#         self.frames.clear()
#         for frame in ImageSequence.Iterator(self.original_gif):
#             img = frame.copy().resize((width, height), Image.Resampling.LANCZOS).convert('RGBA')
#             self.frames.append(ImageTk.PhotoImage(img))

#     def animate(self, idx):
#         if self.frames:
#             self.canvas.delete("bg")
#             self.canvas.create_image(0, 0, image=self.frames[idx], anchor="nw", tags="bg")
#             self.canvas.tag_lower("bg")
#             self.root.after(100, self.animate, (idx + 1) % len(self.frames))

#     def on_resize(self, event):
#         # Only update GIF and reposition when width and height are valid
#         if event.width < 100 or event.height < 100:
#             return
#         self.prepare_frames(event.width, event.height)
#         self.reposition_controls()

#     def build_controls(self):
#         # Create all widgets
#         self._widgets['title'] = tk.Label(self.root, text="Download Organizer",
#                                           font=("yu gothic ui", 24, "bold"), bg="#040405", fg="white")

#         self._widgets['browse'] = tk.Button(self.root, text="Browse Folder", font=("yu gothic ui", 13, "bold"),
#                                             bg="#3047ff", fg="white", activebackground="#2030aa",
#                                             cursor="hand2", command=self.browse_folder)

#         self._widgets['path_lbl'] = tk.Label(self.root, text="No folder selected", font=("yu gothic ui", 11),
#                                              bg="#040405", fg="#aaaaaa", wraplength=600)

#         self._widgets['start'] = tk.Button(self.root, text="Start Organizing", font=("yu gothic ui", 13, "bold"),
#                                            bg="#2e7d32", fg="white", activebackground="#1b5e20",
#                                            cursor="hand2", command=self.start_clicked)

#         self._widgets['progress'] = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")

#         self._widgets['status'] = tk.Label(self.root, text="Status: Waiting", font=("yu gothic ui", 10),
#                                            bg="#040405", fg="#bbbbbb")

#     def reposition_controls(self):
#         if not self._widgets:  # If widgets are not yet created, do nothing
#             return

#         # Clear existing window widgets
#         self.canvas.delete("controls")

#         # Get window width and height
#         w = self.canvas.winfo_width()
#         h = self.canvas.winfo_height()
#         cx = w // 2
#         cy = h // 2

#         # Offsets for widget positioning
#         offsets = [-140, -80, -40, 20, 80, 120]
#         keys = ['title', 'browse', 'path_lbl', 'start', 'progress', 'status']

#         for i, key in enumerate(keys):
#             widget = self._widgets[key]
#             self.canvas.create_window(cx, cy + offsets[i], window=widget, tags="controls")

#     def browse_folder(self):
#         folder = filedialog.askdirectory()
#         if folder:
#             self.selected_path.set(folder)
#             self.path_label.config(text=folder)

#     # def start_clicked(self):
#     #     path = self.selected_path.get()
#     #     if not path:
#     #         self.status_label.config(text="Please select a folder first.")
#     #         return
#     #     self.status_label.config(text="Starting...")
#     #     self.start_callback(path)

#     def start_clicked(self):
#         path = self.selected_path.get()
#         if not path:
#             self.status_label.config(text="Please select a folder first.")
#             return
#         self.status_label.config(text="Starting...")
        
#         # Disable the start button to prevent multiple clicks
#         self._widgets['start'].config(state=tk.DISABLED)
        
#         # Call the sorting function and pass the path
#         self.start_callback(path)


#     def set_progress(self, done, total):
#         self.progress['maximum'] = total
#         self.progress['value'] = done
#         self.status_label.config(text=f"Files processed: {done} of {total}")
#         self.root.update_idletasks()

#     def show_summary(self, moved, skipped, seconds):
#         self.status_label.config(
#             text=f"Completed: moved {moved} files, skipped {skipped} files in {seconds:.2f}s."
#         )


# # For standalone test
# if __name__ == "__main__":
#     def dummy_callback(folder):
#         print("Organizing", folder)
#     root = tk.Tk()
#     app = DownloadOrganizerGUI(root, dummy_callback)
#     root.mainloop()






import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk, ImageSequence


class DownloadOrganizerGUI:
    def __init__(self, root, start_callback):
        self.root = root
        self.root.title("Automated File Organizer ")
        self.root.attributes('-fullscreen', True)
        self.start_callback = start_callback
        self.selected_path = tk.StringVar()

        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.root.bind("<Escape>", lambda e: root.destroy())

        # Load the GIF
        self.gif_path = "background.gif"
        self.original_gif = Image.open(self.gif_path)
        self.frames = []
        self._widgets = {}

        # Widgets for later updates
        self.path_label = None
        self.progress = None
        self.status_label = None

        self.root.after(100, self.initial_setup)

    def initial_setup(self):
        width, height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.prepare_frames(width, height)
        self.animate(0)
        self.build_controls()
        self.root.bind("<Configure>", self.on_resize)

    def prepare_frames(self, width, height):
        self.frames.clear()
        for frame in ImageSequence.Iterator(self.original_gif):
            resized = frame.copy().resize((width, height), Image.Resampling.LANCZOS).convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(resized))

    def animate(self, idx):
        if self.frames:
            self.canvas.delete("bg")
            self.canvas.create_image(0, 0, image=self.frames[idx], anchor="nw", tags="bg")
            self.canvas.tag_lower("bg")
            self.root.after(100, self.animate, (idx + 1) % len(self.frames))

    def build_controls(self):
        cx = self.root.winfo_width() // 2
        cy = self.root.winfo_height() // 2

        # Title
        title = tk.Label(self.root, text="Automated File Organizer",
                         font=("yu gothic ui", 24, "bold"), bg="#040405", fg="white")
        self._widgets['title'] = self.canvas.create_window(cx, cy - 140, window=title)

        # Browse button
        browse = tk.Button(self.root, text="Browse Folder", font=("yu gothic ui", 13, "bold"),
                           bg="#3047ff", fg="white", activebackground="#2030aa",
                           cursor="hand2", command=self.browse_folder)
        self._widgets['browse'] = self.canvas.create_window(cx, cy - 80, window=browse)

        # Path label
        self.path_label = tk.Label(self.root, text="No folder selected", font=("yu gothic ui", 11),
                                   bg="#040405", fg="#aaaaaa", wraplength=600)
        self._widgets['path_lbl'] = self.canvas.create_window(cx, cy - 40, window=self.path_label)

        # Start button
        start = tk.Button(self.root, text="Start Organizing", font=("yu gothic ui", 13, "bold"),
                          bg="#2e7d32", fg="white", activebackground="#1b5e20",
                          cursor="hand2", command=self.start_clicked)
        self._widgets['start'] = self.canvas.create_window(cx, cy + 20, window=start)

        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self._widgets['progress'] = self.canvas.create_window(cx, cy + 80, window=self.progress)

        # Status label
        self.status_label = tk.Label(self.root, text="Status: Waiting", font=("yu gothic ui", 10),
                                     bg="#040405", fg="#bbbbbb")
        self._widgets['status'] = self.canvas.create_window(cx, cy + 120, window=self.status_label)

    def on_resize(self, event):
        if not self._widgets:
            return
        self.reposition_controls()

    def reposition_controls(self):
        cx = self.root.winfo_width() // 2
        cy = self.root.winfo_height() // 2

        offsets = {
            'title': -140,
            'browse': -80,
            'path_lbl': -40,
            'start': 20,
            'progress': 80,
            'status': 120
        }

        for key, offset in offsets.items():
            widget_id = self._widgets.get(key)
            if widget_id:
                self.canvas.coords(widget_id, cx, cy + offset)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_path.set(folder)
            if self.path_label:
                self.path_label.config(text=folder)

    def start_clicked(self):
        path = self.selected_path.get()
        if not path:
            if self.status_label:
                self.status_label.config(text="Please select a folder first.")
            return
        if self.status_label:
            self.status_label.config(text="Starting...")
        self.start_callback(path)

    def set_progress(self, done, total):
        if self.progress and self.status_label:
            self.progress['maximum'] = total
            self.progress['value'] = done
            self.status_label.config(text=f"Files processed: {done} of {total}")
            self.root.update_idletasks()

    def show_summary(self, moved, skipped, seconds):
        if self.status_label:
            self.status_label.config(
                text=f"Completed: moved {moved} files, skipped {skipped} files in {seconds:.2f}s."
            )


# For test
if __name__ == "__main__":
    def dummy_start(path): print("Organizing:", path)
    root = tk.Tk()
    gui = DownloadOrganizerGUI(root, dummy_start)
    root.mainloop()
