# Это тестовый файл
import os
if int(input()) == 1:
    def create_folder(name:str):
        """creates a directory without intermediate directories"""
        folder = os.mkdir(name, mode=0o777,  dir_fd=None)
        print("вызвон инструмент create_folder")
        print()
        if folder == None:
            return "folder created successfully"
        else:
            return "The folder was not created, it already exists."
    print("1")
create_folder("gol")