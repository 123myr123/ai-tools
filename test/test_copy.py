# Это тестовый файл
import os
t =0
if t ==1:
    def create_folder(name:str):
        """creates a directory without intermediate directories"""
        folder = os.mkdir(name, mode=0o777,  dir_fd=None)
        print("вызвон инструмент create_folder")
        print()
        if folder == None:
            return "folder created successfully"
        else:
            return "The folder was not created, it already exists."
else:
    def create_folder(name:str):
        """creates a directory without intermediate directories"""
        print("вызвон инструмент create_folder")
        print()
        if input("Y/N") == "Y":
            folder = os.mkdir(name, mode=0o777,  dir_fd=None)
            if folder == None:
                return "folder created successfully"
            else:
                return "The folder was not created, it already exists."
        else:
            return "no"
