from pathlib import Path
import os
import subprocess
import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, filename="app.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')
def json_data(name:str,tipe:str):
    """читает json конфиг"""
    with open('tools_config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        x = data[name]
    return(x[tipe])

def run_comand(name:str):
    """Executes the command specified in the command name. It waits for the command to complete and then displays the result. If input is required during the call, the user enters it."""
    logging.info("вызвон инструмент run_comand")
    for ban in json_data("run_comand","ban_list"):
        if ban == name:
            logging.info("Откланено, команда в бан листе")
            return "rejected by the system"
    for ask in json_data("run_comand","ask_list"):
        if ask == name:
            print("ии хочет вызвать команду " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                command = subprocess.check_output(name, universal_newlines=True)
                logging.info("User одобрил вызов команды " +name,)
                logging.info(command)
                return command
            else: 
                logging.info("User откланил вызов команды")
                return "denied by user"
    access = json_data("run_comand","access")
    if access == 2:    
            command = subprocess.check_output(name, universal_newlines=True)
            logging.info("вызов команды: " +name,)
            logging.info(command)
            return command
    elif access == 1:
            print("ии хочет вызвать команду " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                command = subprocess.check_output(name, universal_newlines=True)
                logging.info("User одобрил вызов команды " +name, "результат команды: " +command)
                logging.info(command)
                return command
            else: 
                logging.info("User откланил вызов команды")
                return "denied by user"
    else:
            logging.warning("Ошибка доступа проверьте tools_config.json")
            return "The tool is not available due to incorrect user settings."

def create_folder(name:str):
    """creates a directory without intermediate directories"""
    logging.info("вызвон инструмент create_folder")
    for ban in json_data("create_folder","ban_list"):
        if ban == name:
            logging.info("Откланено это име в бан листе:")
            return "rejected by the system"
    for ask in json_data("create_folder","ask_list"):
        if ask == name:
            print("ии хочет создать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                folder = os.mkdir(name, mode=0o777,  dir_fd=None)
                if folder == None:
                    logging.info("User одобрил создание папки: " +name)
                    return "folder created successfully"
                else:
                    logging.warning("папка не создана ошибка: " +folder)
                    return "The folder was not created, it already exists."
            else: 
                logging.info("User откланил вызов команды")
                return "denied by user"
    access = json_data("create_folder","access")
    if access == 2:    
            folder = os.mkdir(name, mode=0o777,  dir_fd=None)
            if folder == None:
                    logging.info("User одобрил создание папки: " +name)
                    return "folder created successfully"
            else:
                    logging.warning("папка не создана ошибка: " +folder)
                    return "The folder was not created, it already exists."
    elif access == 1:
            print("ии хочет создать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                folder = os.mkdir(name, mode=0o777,  dir_fd=None)
                if folder == None:
                    logging.info("User одобрил создание папки: " +name)
                    return "folder created successfully"
                else:
                    logging.warning("папка не создана ошибка: " +folder)
                    return "The folder was not created, it already exists."
            else: 
                logging.info("User откланил вызов команды")
                return "denied by user"
    else:
        logging.warning("Ошибка доступа проверьте tools_config.json")
        return "The tool is not available due to incorrect user settings."



def read_folder(name: str):
    """List of files and directories in a folder. The dot (.) symbol shows directories and files in the root folder."""
    logging.info("вызвон инструмент read_folder")
    for ban in json_data("read_folder","ban_list"):
        if ban == name:
            logging.info("чтение даный папки запрешено:" +name)
            return "rejected by the system"
    for ask in json_data("read_folder","ask_list"):
        if ask == name:
            print("ии хочет прочитать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                logging.info("User одобрил чтение папки " +name)
                logging.info(os.listdir(path= name))
                return (os.listdir(path= name))
            else: 
                logging.info("User откланил чтение папки")
                return "denied by user"
    access = json_data("read_file","access")
    if access == 2:    
                logging.info("User одобрил чтение папки " +name)
                logging.info(os.listdir(path= name))
                return (os.listdir(path= name))
    elif access == 1:
            print("ии хочет прочитать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                logging.info("User одобрил чтение папки " +name)
                logging.info(os.listdir(path= name))
                return (os.listdir(path= name))
            else: 
                logging.info("User откланил чтение папки")
                return "denied by user"
    else:
        logging.warning("Ошибка доступа проверьте tools_config.json")
        return "The tool is not available due to incorrect user settings."
    
def write_file(name: str, content: str):
    """open for writing, file contents are deleted, if the file does not exist, a new one is created"""
    logging.info("вызвон инструмент write_file")
    for ban in json_data("write_file","ban_list"):
        if ban == name:
            logging.info("чтение файла запрешено")
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
                logging.info("User одобрил запись файла " +name)
                logging.info(content)
                return "information recorded"
            else: 
                logging.info("User откланил запись файла " +name)
                return "denied by user"
    access = json_data("write_file","access")
    if access == 2:    
                file = open(name,'w', encoding='utf-8')
                file.write(content)
                file.close
                logging.info("User одобрил запись файла " +name)
                logging.info(content)
                return "information recorded"
    elif access == 1:
            print("ии хочет изменить файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name,'w', encoding='utf-8')
                file.write(content)
                file.close
                logging.info("User одобрил запись файла " +name, " с контемтом: " +content)
                return "information recorded"
            else: 
                logging.info("User откланил запись файла " +name)
                return "denied by user"
    else:
        logging.warning("Ошибка доступа проверьте tools_config.json")
        return "The tool is not available due to incorrect user settings."



def read_file(name: str):
    """Read the specified file. Returns the file contents."""
    logging.info("вызвон инструмент read_file")
    for ban in json_data("read_file","ban_list"):
        if ban == name:
            return "rejected by the system"
    for ask in json_data("read_file","ask_list"):
        if ask == name:
            print("ии хочет прочитать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name, 'r', encoding='utf-8')
                logging.info("user одоюрил чтение файла " +name)
                return file.read()
            else: 
                logging.info("User откланил чтение файла " +name)
                return "denied by user"
    access = json_data("read_file","access")
    print (access)
    if access == 2:    
        file = open(name, 'r', encoding='utf-8')
        logging.info("чтение файла " +name)
        return file.read()
    elif access == 1:
            print("ии хочет прочитать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name, 'r', encoding='utf-8')
                logging.info("user одоюрил чтение файла " +name)
                return file.read()
            else: 
                logging.info("User откланил чтение файла " +name)
                return "denied by user"
    else:
        logging.warning("Ошибка доступа проверьте tools_config.json")
        return "The tool is not available due to incorrect user settings."

def create_file(name: str, content: str):
    """Create a file with the given name and content."""
    logging.info("вызвон инструмент create_file")
    for ban in json_data("create_file","ban_list"):
        if ban == name:
            logging.info("создание файла отклонено име в бан листе")
            return "rejected by the system"
    for ask in json_data("create_file","ask_list"):
        if ask == name:
            print("ии хочет создать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                dest_path = Path(name)
                if dest_path.exists():
                    logging.warning("Error: File already exists.")
                    return "Error: File already exists."
                try:
                    dest_path.write_text(content, encoding="utf-8")
                    logging.info("User одобрил создание файла " +name)
                    logging.info(content)
                except Exception as exc:
                   logging.error("Error: {exc!r}")
                   return "Error: {exc!r}"
                return "File created."
            else: 
                logging.info("user откланил создание файла")
                return "denied by user"
    access = json_data("create_file","access")
    if access == 2:    
                dest_path = Path(name)
                if dest_path.exists():
                    logging.warning("Error: File already exists.")
                    return "Error: File already exists."
                try:
                    dest_path.write_text(content, encoding="utf-8")
                    logging.info("создание файла " +name)
                    logging.info(content)
                except Exception as exc:
                   logging.error("Error: {exc!r}")
                   return "Error: {exc!r}"
                return "File created."
    elif access == 1:
            print("ии хочет создать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                dest_path = Path(name)
                if dest_path.exists():
                    logging.warning("Error: File already exists.")
                    return "Error: File already exists."
                try:
                    dest_path.write_text(content, encoding="utf-8")
                    logging.warning("User одобрил создание файла " +name," с контентом " +content)
                except Exception as exc:
                   logging.error("Error: {exc!r}")
                   return "Error: {exc!r}"
                return "File created."
            else: 
                logging.info("user откланил создание файла")
                return "denied by user"
    else:
        logging.warning("Ошибка доступа проверьте tools_config.json")
        return "The tool is not available due to incorrect user settings."
    
