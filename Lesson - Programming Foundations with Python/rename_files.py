import os
import string

def rename_files():
    #(1) get file names from a folder
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    file_list = os.listdir(r"C:\Users\212312604\Desktop\Udacity - Back End\prank\prank")
    print(file_list)

    #(2) for each file, rename filename
    os.chdir("C:/Users/212312604/Desktop/Udacity - Back End/prank/prank")
    for file_name in file_list:
        print("Old file name "+file_name)
        print("New file name "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
    print("Current Working Directory is "+os.getcwd())


rename_files()
