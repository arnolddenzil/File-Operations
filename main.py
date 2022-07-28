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


def delete_file():
    file_name = input("Enter the name of the file you want to delete : ")
    if os.path.exists(file_name):
        ans = input(f"Are you sure you want to delete the file '{file_name}'? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            os.remove(file_name)
            print(f"File '{file_name}' deleted")
    else:
        print("The file does not exist")
    print("Operation terminated")


def rename_file():
    file_name = input("Enter the name of the file you want to rename : ")
    if os.path.exists(file_name):
        new_name = input("Enter the new name of the file : ")
        ans = input(f"Are you sure you want to rename '{file_name}' to '{new_name}' ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            os.rename(file_name, new_name)
            print(f"File '{file_name}' has been renamed to '{new_name}'")
    else:
        print("The file does not exist")
    print("Operation terminated")


def delete_content_from_file():
    pass


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


def delete_dir():
    folder_name = input("Enter the name of the folder you want to delete : ")

    if os.path.exists(folder_name):
        ans = input(f"Are you sure you want to delete the file '{folder_name}'? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            dir_len = len(os.listdir(folder_name))
            if dir_len > 0:
                ans = input(
                    f"Warning .The directory have {dir_len} items in it. Are you sure you want to delete {folder_name} ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.rmtree(folder_name)
                    print(f"'{folder_name}' has been removed ")
            else:
                shutil.rmtree(folder_name)
                print(f"'{folder_name}' has been removed ")
    else:
        print("The folder does not exist")
    print("Operation terminated")


def rename_dir():
    folder_name = input("Enter the name of the directory you want to rename : ")
    if os.path.exists(folder_name):
        new_name = input("Enter the new name of the directory : ")
        ans = input(f"Are you sure you want to rename '{folder_name}' to '{new_name}' ? : ")
        if ans in ['yes', 'y', 'ok', 'okay']:
            os.rename(folder_name, new_name)
            print(f"Directory '{folder_name}' has been renamed to '{new_name}'")
    else:
        print("The directory does not exist")
    print("Operation terminated")


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
    print("The Drives present are :- ")
    for i in drives:
        print(i[0])

def tell_no_of_items():
    print(f"Number of items in the directory is : {len(os.listdir())}")

def list_all_items():
    for path in os.listdir():
        print(path)

def set_working_location():
    pass

def set_source_dir():
    pass

def set_source_file():
    global source_path
    global source_item_name
    file_name = input("Enter the name of the file : ")
    working_dir = os.getcwd()
    tmp_path = os.path.join(working_dir, file_name)
    if not os.path.exists(tmp_path):
        print("The path does not exist")
    else:
        source_path = tmp_path
        source_item_name = file_name


def set_destination_path():
    global destination_path
    path = input("Enter the name of the file : ")
    working_dir = os.getcwd()
    temp_path = os.path.join(working_dir, path)
    if not os.path.exists(temp_path):
        print("The path does not exist")
    else:
        destination_path = temp_path



def copy_dir_content():
    pass

def paste_dir_content():
    pass

def append_copied_items_to_dir():
    pass

def copy_file_content():
    pass

def paste_file_content():
    pass

def append_copied_content_to_file():
    pass


def copy_operation():
    global source_path
    global destination_path
    if os.path.exists(destination_path):
        if os.path.isfile(destination_path):
            print(os.stat(destination_path).st_size)
            if os.stat(destination_path).st_size == 0:
                shutil.copy2(source_path, destination_path)
            else:
                ans = input(f"The file is not empty. Do you wish to replace the contents of the file ? : ")
                if ans in ['yes', 'y', 'ok', 'okay']:
                    shutil.copy2(source_path, destination_path)
    else:
        print("The destination path was not found")

def move_operation():
    pass

def navigate_forward():
    pass

def hop_back():
    pass

def hop_forward():
    pass


def end_program():
    exit(0)


operations = {
    "1": create_file,
    "2": delete_file,
    "3": rename_file,
    "4": read_file,
    "5": add_text_to_file,
    "6": delete_content_from_file,
    "7": list_file_names,
    "8": tell_no_of_files,
    "9": create_dir,
    "10": delete_dir,
    "11": rename_dir,
    "12": list_dir_names,
    "13": tell_no_of_dir,
    "14": tell_no_of_drives,
    "15": list_drive_names,
    "16": list_all_items,
    "17": tell_no_of_items,
    "18": set_working_location,
    "19": set_source_dir,
    "20": set_source_file,
    "21": set_destination_path,
    "22": copy_dir_content,
    "23": paste_dir_content,
    "24": append_copied_items_to_dir,
    "25": copy_file_content,
    "26": paste_file_content,
    "27": append_copied_content_to_file,
    "28": copy_operation,
    "29": move_operation,
    "30": navigate_forward,
    "31": hop_back,
    "32": hop_forward,
    "33": end_program,
}


print("""
----------------------
    File Operations
    ```````````````
1. Create a new file.
2. Delete a file.
3. Rename a file.
4. Read from a file.
5. Add text to file
6. Delete text from file.
7. List file names
8. Tell number of files
9. Create Directory
10. Delete Directory
11. Rename Directory
12. List Directory names
13. Tell number of directories
14. Tell number of drives
15. List drive names
16. List all items in the directory
17. Tell number of items
18. Set working location
19. Set source directory
20. Set source file
21. Set destination path
22. Copy directory content from source directory
23. Paste directory content to the destination directory
24. Append copied directory items to the destination directory
25. Copy file content from source file
26. Paste file content to destination file
27. Append copied content to destination file
28. Do copy operation
29. Do move/transfer operation
30. Navigate forward
31. Hop back a few steps
32. Hop forward
33. Exit 
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



