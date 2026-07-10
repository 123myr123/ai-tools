from pathlib import Path
import os
import subprocess
import json
import logging
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

logging.basicConfig(level=logging.INFO, filename="app.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')
def chek_list_tools(name:str,pyti:str):
        """"Проверки безопастности"""
        for ban in json_data(name,"ban_list"):
            rel_path = Path(pyti)
            abs_path = rel_path.resolve()
            ban_path = Path(ban)
            abs_ban = ban_path.resolve()
            if abs_ban == abs_path:
                return 1
        for ask in json_data(name,"ask_list"):
            rel_path = Path(pyti)
            abs_path = rel_path.resolve()
            ask_path = Path(ask)
            abs_ask = ask_path.resolve()
            if abs_ask == abs_path:
                return 2
        rel_path = Path(pyti)
        abs_path = rel_path.resolve()
        if not "ai-tools" in str(abs_path) :
            with open('tools_config.json', 'r', encoding='utf-8') as file:
                workspace = json.load(file)
                for folder in workspace["workspace"]:
                    rel_foldre = Path(folder)
                    abs_folder = rel_foldre.resolve()
                    if str(abs_folder) in str(abs_path):
                        return None
            return 1
def json_data(name:str,tipe:str):
    """читает json конфиг"""
    with open('tools_config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        x = data[name]
    return(x[tipe])


def search_duckduckgo(search:str):
    """Sends a request to the DuckDuckGo service."""
    logging.info("Начат поиск по запросу: " +search)
    with DDGS() as ddgs:
        logging.info("Поиск завершон")
        return ddgs.text(search,max_results= 10)
        
def extract_text_from_url(url:str):
    """
    Extracts and saves the plain text content from the specified URL.
    """
    logging.info("Вызван инструмент extract_text_from_url. Ссылка: " +url)
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # выбросит исключение при HTTP-ошибке
        soup = BeautifulSoup(response.text, 'html.parser')
        for element in soup(["script", "style"]):
            element.decompose()
        raw_text = soup.get_text(separator='\n', strip=True)
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        clean_text = '\n'.join(lines)
        return clean_text
    except requests.exceptions.RequestException as e:
        logging.info(f"Ошибка при запросе: {e}")
        return (f"Ошибка при запросе: {e}")
    except Exception as e:
        logging.info(f"Неожиданная ошибка: {e}")
        return (f"Неожиданная ошибка: {e}")

def run_command(name:str):
    """Executes the command specified in the command name. It waits for the command to complete and then displays the result. If input is required during the call, the user enters it."""
    logging.info("вызвон инструмент run_comand")
    for ban in json_data("run_command","ban_list"):
        if ban in name:
            logging.info("Откланено, команда в бан листе")
            return "rejected by the system"
    for ask in json_data("run_command","ask_list"):
        if ask in name:
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
    access = json_data("run_command","access")
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
                logging.info("User одобрил вызов команды " +name)
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
    chek = chek_list_tools("create_folder",name)
    if chek == 1:
            logging.info("создание данной папки запрешено" +name)
            return "rejected by the system"
    elif chek == 2:
        print("ии хочет создать папку: " +name)
        print("Y/N")
        x = input()
        if x == "Y" or x =="y":
            try:
                folder = os.mkdir(name, mode=0o766,  dir_fd=None)
                logging.info("user одобрил создание папки " +name)
            except FileExistsError:
                logging.error("Попытка создать существующию папку")
                return "Error: Попытка создать существующию папку"
            return "Folder created."
        else: 
            logging.info("User откланил вызов команды")
            return "denied by user"
    access = json_data("create_folder","access")
    if access == 2:    
            try:
                folder = os.mkdir(name, mode=0o766,  dir_fd=None)
                logging.info("user одобрил создание папки " +name)
            except Exception as exc:
               logging.error("Error: {exc!r}")
               return "Error: {exc!r}"
            return "File created."
    elif access == 1:
            print("ии хочет создать папку: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                folder = os.mkdir(name, mode=0o766,  dir_fd=None)
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
    chek = chek_list_tools("read_folder",name)
    if chek == 1:
            logging.info("чтение даный папки запрешено:" +name)
            return "rejected by the system"
    elif chek == 2:
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
    access = json_data("read_folder","access")
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

    chek = chek_list_tools("write_file",name)
    if chek == 1:
                logging.info("чтение даный папки запрешено:" +name)
                return "rejected by the system"
    elif chek == 2:
                print("ии хочет изменить файл: " +name)
                print("Y/N")
                x = input()
                if x == "Y" or x =="y":
                    file = open(name,'w', encoding='utf-8')
                    file.write(content)
                    file.close()
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
                file.close()
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
                file.close()
                logging.info("User одобрил запись файла " +name)
                logging.info(content)
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
    chek = chek_list_tools("read_file",name)
    if chek == 1:
            logging.info("чтение даного  файла запрешено:" +name)
            return "rejected by the system"
    elif chek == 2:
            print("ии хочет прочитать файл: " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name, 'r', encoding='utf-8')
                logging.info("user одобрил чтение файла " +name)
                return file.read()
            else: 
                logging.info("User откланил чтение файла " +name)
                return "denied by user"

    access = json_data("read_file","access")
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
    chek = chek_list_tools("create_folder",name)
    if chek == 1:
            logging.info("создание файла отклонено име в бан листе")
            return "rejected by the system"
    elif chek == 2:
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
    
