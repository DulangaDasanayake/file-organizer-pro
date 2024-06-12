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

# Create folders for each category
for category in categories:
    category_path = os.path.join(target_folder, category)
    if not os.path.exists(category_path):
        os.mkdir(category_path)

# Function to categorize and move files
def categorize_and_move_files(target_folder, categories):
    for item in os.listdir(target_folder):
        if os.path.isfile(os.path.join(target_folder, item)):
            file_extension = item.split('.')[-1].lower()
            moved = False
            for category, extensions in categories.items():
                if file_extension in extensions:
                    shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, category, item))
                    moved = True
                    break
            # Move to 'Others' if the file type doesn't match any category
            if not moved:
                shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, 'Others', item))

# Call the function to categorize and move files
categorize_and_move_files(target_folder, categories)

print("Files have been categorized and moved successfully.")
