import os
import shutil
import win32api

source_path = ""
source_item_name = ""
destination_path = ""


def create_file():
    file_name = input("What should be the file name? : ")
    try:
        f = open(file_name, 'x')
        f.close()
        print(f"File '{file_name}' created.")
    except FileExistsError:
        ans = input("The file already exist, do you want to overwrite it ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            f = open(file_name, 'w')
            f.close()
            print("File Created")
        else:
            print("Operation terminated")
            return
    ans = input(f"Would you like to add some text to {file_name}? : ")
    if ans in ['yes', 'y', 'ok', 'okay']:
        text = input("What would you like to add ? : ")
        with open(file_name, 'a') as f:
            f.write(text)
            f.write('\n')
        ans = input("Do you want to see the entered text ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            with open(file_name, 'r') as f:
                print("File content : ", f.read())
            print("Operation complete")
        else:
            print("Operation terminated")
            return
    else:
        print("Operation terminated")
        return


def read_file():
    file_name = input("Enter the name of the file you want to read from : ")
    try:
        f = open(file_name, "r")
        print("File content : \n", f.read())
        f.close()
    except FileNotFoundError:
        print(f"File '{file_name}' not found in the current working directory.")
    finally:
        print("Operation terminated")


def rename_item():
    item_name = input("Enter the name of the file you want to rename : ")
    if os.path.exists(item_name):
        new_name = input("Enter the new name of the file : ")
        ans = input(f"Are you sure you want to rename '{item_name}' to '{new_name}' ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            os.rename(item_name, new_name)
            print(f"'{item_name}' has been renamed to '{new_name}'")
    else:
        print("The item does not exist")
    print("Operation terminated")


def add_text_to_file():
    file_name = input("Enter the name of the file you want to add text to : ")
    if os.path.exists(file_name):
        text = input("What would you like to add ? : ")
        with open(file_name, 'a') as f:
            f.write(text)
            f.write('\n')
        print("Operation Completed")
    else:
        print("The file does not exist")
        print("Operation terminated")


def list_file_names():
    for path in os.listdir():
        # check if current path is a file
        if os.path.isfile(path):
            print(path)


def tell_no_of_files():
    no_of_files = 0
    for path in os.listdir():
        # check if current path is a file
        if os.path.isfile(path):
            no_of_files += 1

    print(f"Number of files preset is : {no_of_files}")


def create_dir():
    folder_name = input("What should be the folder name? : ")
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        ans = input("The folder already exist, do you want to overwrite it ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            dir_len = len(os.listdir(folder_name))
            if dir_len > 0:
                ans = input(
                    f"Warning .The directory have {dir_len} items in it. Are you sure you want to overwrite it ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.rmtree(folder_name)
                    os.mkdir(folder_name)
            else:
                shutil.rmtree(folder_name)
                os.mkdir(folder_name)


def delete_item():
    item_name = input("Enter the name of the item you want to delete : ")
    if os.path.exists(item_name):
        if os.path.isfile(item_name):
            ans = input(f"Are you sure you want to delete the file '{item_name}'? : ")
        else:
            ans = input(f"Are you sure you want to delete the folder '{item_name}'? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            try:
                os.remove(item_name)
            except PermissionError:
                shutil.rmtree(item_name)
                print(f"Folder '{item_name}' deleted ")
            else:
                print(f"File '{item_name}' deleted")
    else:
        print("The path does not exist. Operation terminated")



def list_dir_names():
    for path in os.listdir():
        # check if current path is a file
        if not os.path.isfile(path):
            print(path)


def tell_no_of_dir():
    no_of_dir = 0
    for path in os.listdir():
        # check if current path is a file
        if not os.path.isfile(path):
            no_of_dir += 1
    print(f"Number of directories preset is : {no_of_dir}")


def tell_no_of_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    no_of_drives = len(drives)
    print(f"Number of drives present in the computer is '{no_of_drives}' ")


def list_drive_names():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)
    output = ''
    if len(drives) > 1:
        print("The Drives present are :- ")
        for i in range(len(drives)-1):
            output += f"{drives[i][0]} "
        output += f"and {drives[i+1][0]}"
        print(output)
    else:
        output = drives[0][0]
        print(f"The only drive present in the system is {output} drive")



def tell_no_of_items():
    print(f"Number of items in the directory is : {len(os.listdir())}")


def list_all_items():
    for path in os.listdir():
        print(path)


def set_working_location():
    name_major = input("Where should i set the current working directory")
    print(f"Current working directory before hopping inside {name_major}")
    print(os.getcwd())
    # if name_major == 'c drive':
    #     path_major = r'C:'
    # elif new
    locations = {
        'c drive': r'C:',
        'd drive': r'D:',
        'e drive': r'E:',
        'f drive': r'F:',
        'downloads': r'C:\Users\Arnold\Downloads',
        'documents': r'C:\Users\Arnold\Documents',
        'pictures': r'C:\Users\Arnold\Pictures',
        'music': r'C:\Users\Arnold\Music',
        'movies': r'E:\Movies',
        'games': r'D:\TodeleteGames'
    }
    try:
        path_major = locations[name_major]
    except KeyError:
        print("Unfortunately i cannot set the working location there automatically")
    else:
        try:
            os.chdir(path_major)
        except NotADirectoryError:
            print(f"'{name_major}' is not a directory.")
        else:
            print(f"Current working directory after hopping inside {name_major}")
            print(os.getcwd())


def set_source_path():
    global source_path
    global source_item_name
    file_name = input("What is the name of the source path ? : ")
    working_dir = os.getcwd()
    tmp_path = os.path.join(working_dir, file_name)
    if not os.path.exists(tmp_path):
        print("The path does not exist")
    else:
        source_path = tmp_path
        source_item_name = file_name
        print("Source path is set")


def set_destination_path():
    global destination_path
    path = input("What is the name of the destination path ? : ")
    working_dir = os.getcwd()
    temp_path = os.path.join(working_dir, path)
    if not os.path.exists(temp_path):
        print("The path does not exist")
    else:
        destination_path = temp_path
        print("Destination path is set")


def copy_operation():
    global source_item_name
    global source_path
    global destination_path
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
                if destination_path[len_of_dest_path - len_of_source_item_name:] == source_item_name:
                    ans = input("The file already exist. Do you wish to overwrite it ? : ")
                    if ans in ['yes', 'y', 'ok', 'okay']:
                        shutil.copy2(source_path, destination_path)
                        print("Copy operation completed")
                    else:
                        print("Copy Operation terminated")
                else:
                    if os.stat(destination_path).st_size == 0:
                        shutil.copy2(source_path, destination_path)
                        print("Copy operation completed")
                    else:
                        ans = input(f"The file is not empty. Do you wish to replace the contents of the file ? : ")
                        if ans in ['yes', 'y', 'ok', 'okay']:
                            shutil.copy2(source_path, destination_path)
                            print("Copy operation completed")
                        else:
                            print("Copy Operation terminated")
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
                        print("Copy operation completed")
                    else:
                        print("Copy Operation terminated")
                else:
                    shutil.copy2(source_path, destination_path)
                    print("Copy operation completed")

        else:
            if os.path.isfile(destination_path):
                print("Cannot copy folder to file")
            else:
                item_exist_in_folder = False
                for item in os.listdir(destination_path):
                    if item == source_item_name:
                        item_exist_in_folder = True
                if item_exist_in_folder:
                    ans = input("A folder with the same name already exist. Do you wish to overwrite it ? : ")
                    if ans in ['yes', 'y', 'ok', 'okay']:
                        destination_path = rf'{destination_path}\{source_item_name}'
                        shutil.rmtree(destination_path)
                        shutil.copytree(source_path, destination_path)
                        print("Copy operation completed")
                    else:
                        print("Copy Operation terminated")
                else:
                    destination_path = rf'{destination_path}\{source_item_name}'
                    shutil.copytree(source_path, destination_path)
                    print("Copy operation completed")


def move_operation():
    global source_item_name
    global source_path
    global destination_path
    if not os.path.exists(source_path) and not os.path.exists(destination_path):
        print("The source and destination path does not exist or is not set")
    elif not os.path.exists(source_path):
        print("Source path does not exist")
    elif not os.path.exists(destination_path):
        print("Destination path does not exist")
    else:
        if os.path.isfile(source_path):
            if os.path.isfile(destination_path):
                print("Cannot move a file into a file. Operation terminated")
            else:
                item_exist_in_folder = False
                for item in os.listdir(destination_path):
                    if item == source_item_name:
                        item_exist_in_folder = True
                if item_exist_in_folder:
                    ans = input("An item with the same name already exist. Do you wish to overwrite it ? : ")
                    if ans in ['yes', 'y', 'ok', 'okay']:
                        destination_path = rf'{destination_path}\{source_item_name}'
                        try:
                            os.remove(destination_path)
                        except PermissionError:
                            shutil.rmtree(destination_path)
                        finally:
                            shutil.move(source_path, destination_path)
                            print("Move operation completed")
                    else:
                        print("Move Operation terminated")
                else:
                    shutil.move(source_path, destination_path)
                    print("Move operation completed")
        else:
            if os.path.isfile(destination_path):
                print("Cannot move folder to file")
            else:
                item_exist_in_folder = False
                for item in os.listdir(destination_path):
                    if item == source_item_name:
                        item_exist_in_folder = True
                if item_exist_in_folder:
                    ans = input("A folder with the same name already exist. Do you wish to overwrite it ? : ")
                    if ans in ['yes', 'y', 'ok', 'okay']:
                        destination_path = rf'{destination_path}\{source_item_name}'
                        shutil.rmtree(destination_path)
                        shutil.move(source_path, destination_path)
                        print("Move operation completed")
                    else:
                        print("Move Operation terminated")
                else:
                    destination_path = rf'{destination_path}\{source_item_name}'
                    shutil.move(source_path, destination_path)
                    print("Move operation completed")


def hop_back():
    print("Current working directory before hopping back")
    print(os.getcwd())
    os.chdir('../')
    print("Current working directory after hopping back")
    print(os.getcwd())


def hop_forward():
    folder = input("Enter the name of the folder you want to hop into : ")
    print(f"Current working directory before hopping inside {folder}")
    print(os.getcwd())
    try:
        os.chdir(folder)
    except NotADirectoryError:
        print(f"'{folder}' is not a directory.")
    else:
        print(f"Current working directory after hopping inside {folder}")
        print(os.getcwd())


def end_program():
    exit(0)


operations = {
    "1": create_file,
    "2": rename_item,
    "3": read_file,
    "4": add_text_to_file,
    "5": list_file_names,
    "6": tell_no_of_files,
    "7": create_dir,
    "8": delete_item,
    "9": list_dir_names,
    "10": tell_no_of_dir,
    "11": tell_no_of_drives,
    "12": list_drive_names,
    "13": list_all_items,
    "14": tell_no_of_items,
    "15": set_working_location,
    "16": set_source_path,
    "17": set_destination_path,
    "18": copy_operation,
    "19": move_operation,
    "20": hop_back,
    "21": hop_forward,
    "22": end_program,
}


print("""
----------------------
    File Operations
    ```````````````
1. Create a new file.
2. Rename a file.
3. Read from a file.
4. Add text to file
5. List file names
6. Tell number of files
7. Create Directory
8. Delete Directory
9. List Directory names
10. Tell number of directories
11. Tell number of drives
12. List drive names
13. List all items in the directory
14. Tell number of items
15. Set working location
26. Set source path
17. Set destination path
18. Do copy operation
19. Do move/transfer operation
20. Hop back a few steps
21. Hop forward
22. Exit 
""")

again = True

while again:
    try:
        choice = input("Enter your choice : ")
        operations[choice]()
        print('\n')
    except KeyError:
        ask_again = True
        while ask_again:
            choice = input("Please enter one of the provided choices : ")
            try:
                operations[choice]()
            except KeyError:
                pass
            else:
                ask_again = False
    else:
        ans = input(f"Do you want to continue? : ")
        if ans not in ['yes', 'y', 'ok', 'okay']:
            again = False



