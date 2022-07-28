import os

# folder_name = input("Enter the name of the directory you want to rename : ")
# if os.path.exists(folder_name):
#     new_name = input("Enter the new name of the directory : ")
#     ans = input(f"Are you sure you want to rename '{folder_name}' to '{new_name}' ? : ")
#     if ans in ['yes', 'y', 'ok', 'okay']:
#         os.rename(folder_name, new_name)
#         print(f"Directory '{folder_name}' has been renamed to '{new_name}'")
# else:
#     print("The directory does not exist")
# print("Operation terminated")
# working_dir = os.getcwd()
# source_path = os.path.join(working_dir, 'okay')
#
# for path in os.listdir(source_path):
#     # check if current path is a file
#     # if os.path.isfile(path):
#     print(path)

txt = input("Enter : ")
len_txt = len(txt)

vlan = "arnold is great"
len_vlan = len(vlan)

print(vlan[len_vlan-len_txt:])