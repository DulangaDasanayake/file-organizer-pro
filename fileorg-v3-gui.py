import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.directory = tk.StringVar()
        self.directory.set(str(Path.home() / 'Downloads'))
        self.rules = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx'],
            'Music': ['.mp3', '.wav', '.aac', '.flac'],
            'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
            'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
            'Scripts': ['.py', '.js', '.sh', '.bat', '.rb'],
            'Executables': ['.exe', '.msi', '.dmg']
        }
        self.history = []
        self.create_widgets()

    def create_widgets(self):
        # Directory selection
        tk.Label(self.root, text="Directory to organize:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.directory, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_directory).grid(row=0, column=2, padx=10, pady=10)

        # Action buttons
        tk.Button(self.root, text="Organize Files", command=self.organize).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Undo Last Action", command=self.undo).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Add Rule", command=self.add_rule).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text="View Rules", command=self.view_rules).grid(row=1, column=3, padx=10, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=1, column=4, padx=10, pady=10)

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
                if destination_folder:
                    destination = directory / destination_folder
                    destination.mkdir(exist_ok=True)
                    shutil.move(str(file_path), destination / file_path.name)
                    self.history.append((file_path, destination / file_path.name))
        messagebox.showinfo("File Organizer", "Files have been organized.")

    def _get_destination_folder(self, file_extension):
        for folder, extensions in self.rules.items():
            if file_extension.lower() in extensions:
                return folder
        return None

    def undo(self):
        if not self.history:
            messagebox.showinfo("File Organizer", "No actions to undo.")
            return
        
        for original_path, new_path in reversed(self.history):
            shutil.move(str(new_path), original_path)
        self.history = []
        messagebox.showinfo("File Organizer", "Undo completed. Files have been moved back to their original locations.")

    def add_rule(self):
        rule_window = tk.Toplevel(self.root)
        rule_window.title("Add Rule")
        
        tk.Label(rule_window, text="Folder Name:").grid(row=0, column=0, padx=10, pady=10)
        folder_name_entry = tk.Entry(rule_window)
        folder_name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(rule_window, text="File Extensions (comma separated):").grid(row=1, column=0, padx=10, pady=10)
        extensions_entry = tk.Entry(rule_window)
        extensions_entry.grid(row=1, column=1, padx=10, pady=10)
        
        def add_rule_action():
            folder_name = folder_name_entry.get()
            extensions = extensions_entry.get().split(',')
            self.add_rule_to_dict(folder_name, extensions)
            rule_window.destroy()
        
        tk.Button(rule_window, text="Add Rule", command=add_rule_action).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_rule_to_dict(self, folder_name, extensions):
        if folder_name in self.rules:
            self.rules[folder_name].extend([ext.strip() for ext in extensions])
        else:
            self.rules[folder_name] = [ext.strip() for ext in extensions]

    def view_rules(self):
        rules_window = tk.Toplevel(self.root)
        rules_window.title("View Rules")
        
        for idx, (folder, extensions) in enumerate(self.rules.items(), start=1):
            rule_label = tk.Label(rules_window, text=f"{idx}. {folder}: {', '.join(extensions)}")
            rule_label.pack(padx=10, pady=5)

def main():
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
