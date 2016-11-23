import os

def rename_files():

    file_list = os.listdir("/Users/lilu/Downloads/prank")
    save_path = os.getcwd()
    os.chdir("/Users/lilu/Downloads/prank")
    for file_name in file_list:
        print("Old name : " + file_name)
        print("New name : " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)
rename_files()
