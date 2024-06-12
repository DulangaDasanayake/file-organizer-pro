import os
import shutil

# Define the target folder
target_folder = 'C:/Users/Samsung/Downloads'

# Define categories and their respective extensions
categories = {
    'Pictures': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg'],
    'Videos': ['mp4', 'mov', 'wmv', 'flv', 'avi', 'mkv'],
    'Documents': ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'odt'],
    'Music': ['mp3', 'wav', 'aac', 'flac', 'ogg'],
    'Archives': ['zip', 'rar', '7z', 'tar', 'gz'],
    'Scripts': ['py', 'js', 'html', 'css'],
    'Others': []
}

# Define destination paths for each category
destination_paths = {
    'Pictures': 'C:/Users/Public/Pictures',
    'Documents': 'C:/Users/Public/Documents',
    'Videos': 'C:/Users/Samsung/Videos',  # Adjust path as needed
    'Music': 'C:/Users/Samsung/Music',    # Adjust path as needed
    'Archives': 'C:/Users/Public/Documents',  # Send to Documents
    'Scripts': 'C:/Users/Public/Documents',    # Send to Documents
    'Others': 'C:/Users/Public/Documents'      # Send to Documents
}

# Create folders for each category if they don't exist
for category, path in destination_paths.items():
    if not os.path.exists(path):
        os.makedirs(path)

# Function to categorize and move files
def categorize_and_move_files(target_folder, categories, destination_paths):
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(os.path.join(target_folder, item), os.path.join(destination_paths[category], item))
                    moved = True
                    break
            # Move to 'Others' if the file type doesn't match any category
            if not moved:
                shutil.move(os.path.join(target_folder, item), os.path.join(destination_paths['Others'], item))

# Call the function to categorize and move files
categorize_and_move_files(target_folder, categories, destination_paths)

print("Files have been categorized and moved successfully.")
