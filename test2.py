import os
import shutil
import win32api

file_name = input("Enter the name of the file : ")
working_dir = os.getcwd()
tmp_path = os.path.join(working_dir, file_name)
source_path=tmp_path
source_item_name = file_name

# destination_path = os.path.join(working_dir, 'okay', 'bc')
destination_path = r'E:\Extra Projects\File_Operations\bro'

if not os.path.exists(source_path) and not os.path.exists(destination_path):
    print("The source and destination path does not exist or is not set")
elif not os.path.exists(source_path):
    print("Source path does not exist")
elif not os.path.exists(destination_path):
    print("Destination path does not exist")
else:
    if os.path.isfile(source_path):
        if os.path.isfile(destination_path):
            len_of_dest_path = len(destination_path)
            len_of_source_item_name = len(source_item_name)
            if destination_path[len_of_dest_path-len_of_source_item_name:] == source_item_name:
                ans = input("The file already exist. Do you wish to overwrite it ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.copy2(source_path, destination_path)
            elif os.stat(destination_path).st_size == 0:
                shutil.copy2(source_path, destination_path)
                print("Copy operation completed")
            else:
                ans = input(f"The file is not empty. Do you wish to replace the contents of the file ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.copy2(source_path, destination_path)
        else:
            item_exist_in_folder = False
            print(os.listdir(destination_path))
            for item in os.listdir(destination_path):
                if item == source_item_name:
                    item_exist_in_folder = True
            if item_exist_in_folder:
                ans = input("The file already exist. Do you wish to overwrite it ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.copy2(source_path, destination_path)
            else:
                shutil.copy2(source_path, destination_path)

    else:
        try:
            shutil.copytree(source_path, destination_path)
        except FileExistsError:
            print("The destination folder already exist")
            




# print(source_path)
