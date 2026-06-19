import json
from pdb import run

def json_data(name:str,tipe:str):
# Открываем файл с указанием кодировки UTF-8
    with open('test.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print (name)
        print (tipe)

        x = data[name]
        print(x[tipe])
    return(x[tipe])


def read_file(name: str):
    """Read the specified file. Returns the file contents."""
    access = json_data("read_file","dostyp")
    print("вызвон инструмент read_file")
    print()
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
        print (read_file("test_copy.py"))