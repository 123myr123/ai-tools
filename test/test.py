# Это тестовый файл
import os
import subprocess
import logging
import json
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')

def json_data(name:str,tipe:str):
    """читает json конфиг"""
    with open('tools_config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        x = data[name]
        print(x[tipe])
    return(x[tipe])

def read_file(name: str):
    """Read the specified file. Returns the file contents."""
    access = json_data("read_file","access")
    logging.info("вызвон инструмент read_file")
    for ban in json_data("read_file","ban_list"):
        if ban == name:
            print(ban)
            return "в доступе отказано"
    for ask in json_data("read_file","ask_list"):
        if ask == name:
            print("ии хочет вызвать команду " +name)
            print("Y/N")
            x = input()
            if x == "Y" or x =="y":
                file = open(name)
                return file.read()
            else: 
                return "В доступе отказано"
    print(access)
    if access == 2:    
        file = open(name)
        return file.read()
    elif access == 1:
        print("ии хочет вызвать команду " +name)
        print("Y/N")
        x = input()
        if x == "Y" or x =="y":
            file = open(name)
            return file.read()
        else: 
            return "В доступе отказано"
    else:
        return "В доступе отказано"


while True:
    if int(input()) == 1:
        break
    else:
        print (read_file("test-json.py"))