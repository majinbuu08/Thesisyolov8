import shutil

# Path of the folder to be zipped
folder_path = "C:\\Users\\jdich\\thesisnew\\runs"

# Path of the zip file to be created
zip_file_path = "C:\\Users\\jdich\yolo"

# Create the zip file
shutil.make_archive(zip_file_path[:-4], 'zip', folder_path)