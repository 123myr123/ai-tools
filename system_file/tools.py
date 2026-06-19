from pathlib import Path
import os
import subprocess
import json
from pathlib import Path

def json_data(name:str,tipe:str):
    """читает json конфиг"""
    with open('tools_config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        x = data[name]
        print(x[tipe])
    return(x[tipe])

def run_comand(name:str):
    """Executes the command specified in the command name. It waits for the command to complete and then displays the result. If input is required during the call, the user enters it."""
    print("вызвон инструмент run_comand")
    for ban in json_data("run_comand","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("run_comand","ask_list"):
        if ask == name:
            print("ии хочет вызвать команду " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                command = subprocess.check_output(name, universal_newlines=True)
                print(command)
                return command
            else: 
                return "denied by user"
    access = json_data("run_comand","access")
    if access == 2:    
            command = subprocess.check_output(name, universal_newlines=True)
            print(command)
            return command
    elif access == 1:
            print("ии хочет вызвать команду " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                command = subprocess.check_output(name, universal_newlines=True)
                print(command)
                return command
            else: 
                return "denied by user"
    else:
            return "The tool is not available due to incorrect user settings."

def create_folder(name:str):
    """creates a directory without intermediate directories"""
    print("вызвон инструмент create_folder")
    print()
    for ban in json_data("create_foldel","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("create_folder","ask_list"):
        if ask == name:
            print("ии хочет создать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                folder = os.mkdir(name, mode=0o777,  dir_fd=None)
                if folder == None:
                    return "folder created successfully"
                else:
                    return "The folder was not created, it already exists."
            else: 
                return "denied by user"
    access = json_data("create_folder","access")
    if access == 2:    
            folder = os.mkdir(name, mode=0o777,  dir_fd=None)
            if folder == None:
                return "folder created successfully"
            else:
                return "The folder was not created, it already exists."
    elif access == 1:
            print("ии хочет создать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                folder = os.mkdir(name, mode=0o777,  dir_fd=None)
                if folder == None:
                    return "folder created successfully"
                else:
                    return "The folder was not created, it already exists."
            else: 
                return "denied by user"
    else:
        return "The tool is not available due to incorrect user settings."



def read_folder(name: str):
    """List of files and directories in a folder. The dot (.) symbol shows directories and files in the root folder."""
    print("вызвон инструмент read_folder")
    print()
    for ban in json_data("read_folder","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("read_folder","ask_list"):
        if ask == name:
            print("ии хочет прочитать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                return (os.listdir(path= name))
            else: 
                return "denied by user"
    access = json_data("read_file","access")
    if access == 2:    
        return (os.listdir(path= name))
    elif access == 1:
            print("ии хочет прочитать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                return (os.listdir(path= name))
            else: 
                return "denied by user"
    else:
        return "The tool is not available due to incorrect user settings."
    
def write_file(name: str, content: str):
    """open for writing, file contents are deleted, if the file does not exist, a new one is created"""
    print("вызвон инструмент write_file")
    print()
    for ban in json_data("write_file","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("write_file","ask_list"):
        if ask == name:
            print("ии хочет изменить файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name,'w', encoding='utf-8')
                file.write(content)
                file.close
                return "information recorded"
            else: 
                return "denied by user"
    access = json_data("write_file","access")
    if access == 2:    
            file = open(name,'w', encoding='utf-8')
            file.write(content)
            file.close
            return "information recorded"
    elif access == 1:
            print("ии хочет изменить файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name,'w', encoding='utf-8')
                file.write(content)
                file.close
                return "information recorded"
            else: 
                return "denied by user"
    else:
        return "The tool is not available due to incorrect user settings."



def read_file(name: str):
    """Read the specified file. Returns the file contents."""
    print("вызвон инструмент read_file")
    print()
    for ban in json_data("read_file","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("read_file","ask_list"):
        if ask == name:
            print("ии хочет прочитать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name)
                return file.read()
            else: 
                return "denied by user"
    access = json_data("read_file","access")
    print (access)
    if access == 2:    
        file = open(name)
        return file.read()
    elif access == 1:
            print("ии хочет прочитать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name)
                return file.read()
            else: 
                return "denied by user"
    else:
        return "The tool is not available due to incorrect user settings."

def create_file(name: str, content: str):
    """Create a file with the given name and content."""
    print("вызвон инструмент create_file")
    print()
    for ban in json_data("create_file","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("create_file","ask_list"):
        if ask == name:
            print("ии хочет создать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                dest_path = Path(name)
                if dest_path.exists():
                    return "Error: File already exists."
                try:
                    dest_path.write_text(content, encoding="utf-8")
                except Exception as exc:
                   return "Error: {exc!r}"
                return "File created."
            else: 
                return "denied by user"
    access = json_data("create_file","access")
    if access == 2:    
        dest_path = Path(name)
        if dest_path.exists():
            return "Error: File already exists."
        try:
            dest_path.write_text(content, encoding="utf-8")
        except Exception as exc:
            return "Error: {exc!r}"
        
        return "File created."
    elif access == 1:
            print("ии хочет создать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                dest_path = Path(name)
                if dest_path.exists():
                    return "Error: File already exists."
                try:
                        dest_path.write_text(content, encoding="utf-8")
                except Exception as exc:
                    return "Error: {exc!r}"
                
                return "File created."
            else: 
                return "denied by user"
    else:
        return "The tool is not available due to incorrect user settings."
    
