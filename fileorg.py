import os
import shutil

target_folder = 'C:/Users/Samsung/Downloads'
extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item))}

#create folders for each extension type
for extension in extensions:
    if not os.path.exists(os.path.join(target_folder, extension)):
        os.mkdir(os.path.join(target_folder, extension))

# move files to each folder
for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)):
        file_extension = item.split('.')[-1]
        shutil.move(os.path.join(target_folder, item), os.path.join(target_folder, file_extension, item))
