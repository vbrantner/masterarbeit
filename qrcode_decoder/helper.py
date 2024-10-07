import os


def delete_all_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")


# write function that takes directory name as
# argument and returns a list with directory + filename
def get_all_files_in_folder(folder_path):
    files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                files.append({"path": file_path, "filename": filename})
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
    return files
