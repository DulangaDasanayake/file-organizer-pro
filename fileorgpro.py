import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.configure(bg="#f0f0f0")  # Set background color of the main window
        self.directory = tk.StringVar()
        self.directory.set(str(Path.home() / 'Downloads'))
        self.rules = self.get_all_extensions()
        self.history = []
        self.create_widgets()

    def get_all_extensions(self):
        return {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.ico', '.webp', '.heif', '.avif'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.ppt', '.xls', '.xlsx', '.csv', '.rtf', '.odt', '.ods', '.odp'],
            'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma', '.opus'],
            'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.mpeg', '.3gp'],
            'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.cab', '.iso'],
            'Scripts': ['.py', '.js', '.sh', '.bat', '.rb', '.php', '.pl', '.lua', '.swift', '.ps1'],
            'Executables': ['.exe', '.msi', '.dmg', '.apk', '.appimage'],
            'Code': ['.c', '.cpp', '.h', '.hpp', '.java', '.cs', '.go', '.ts', '.rs', '.kt', '.dart'],
            'Fonts': ['.ttf', '.otf', '.woff', '.woff2'],
            'Disk Images': ['.iso', '.img', '.bin', '.dmg', '.vhd', '.vmdk'],
            'Database': ['.sql', '.sqlite', '.db', '.mdb', '.accdb'],
            '3D Models': ['.obj', '.stl', '.fbx', '.gltf', '.blend'],
            'Torrents': ['.torrent'],
            'Others': []  # Default category for unknown files
        }
    
    def create_widgets(self):
        tk.Label(self.root, text="Directory to organize:", bg="#f0f0f0", fg="#333").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        tk.Entry(self.root, textvariable=self.directory, width=50, bg="#ffffff", fg="#333").grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_directory, bg="#4CAF50", fg="#fff").grid(row=0, column=2, padx=10, pady=10)

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.grid(row=1, column=0, columnspan=3, pady=10)
        tk.Button(button_frame, text="Organize Files", command=self.organize, bg="#2196F3", fg="#fff").grid(row=0, column=0, padx=5, pady=2)
        tk.Button(button_frame, text="Undo Last Action", command=self.undo, bg="#FF5722", fg="#fff").grid(row=0, column=1, padx=5, pady=2)
        tk.Button(button_frame, text="Exit", command=self.root.quit, bg="#f44336", fg="#fff").grid(row=0, column=2, padx=5, pady=2)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory.set(directory)

    def organize(self):
        directory_path = self.directory.get()
        directory = Path(directory_path)
        for file_path in directory.iterdir():
            if file_path.is_file():
                destination_folder = self._get_destination_folder(file_path.suffix)
                destination = directory / destination_folder
                destination.mkdir(exist_ok=True)
                shutil.move(str(file_path), destination / file_path.name)
                self.history.append((file_path, destination / file_path.name))
        messagebox.showinfo("File Organizer", "Files have been organized.")

    def _get_destination_folder(self, file_extension):
        for folder, extensions in self.rules.items():
            if file_extension.lower() in extensions:
                return folder
        return 'Others'  # Default folder for unknown extensions

    def undo(self):
        if not self.history:
            messagebox.showinfo("File Organizer", "No actions to undo.")
            return
        for original_path, new_path in reversed(self.history):
            shutil.move(str(new_path), original_path)
        self.history = []
        messagebox.showinfo("File Organizer", "Undo completed. Files have been moved back to their original locations.")

def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
