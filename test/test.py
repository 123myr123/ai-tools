# Это тестовый файл
import os
import subprocess
import logging
import json
from system_file.tools import *
from pathlib import Path
import lmstudio  as lms
from datetime import datetime

print("Выберите профиль из перечисленых")
for x in read_folder("system_file/profile"):
    print(x)
pyti = input("Выберите профиль: ")

def memory_write(content:str):
     """Writing to the memory module. Entries are preserved between sessions."""

     y = ("system_file/profile/" +pyti)
     h = y + "/"
     pyti_config = h + "memory.txt"
     file = open(pyti_config,'w', encoding='utf-8')
     file.write(content)
     file.close
     return "The information has been recorded."

def memory_read():
    """reads the memory module"""
    y = ("system_file/profile/" +pyti)
    h = y + "/"
    pyti_config = h + "memory.txt"
    with open(pyti_config, "r", encoding='utf-8') as file:
        return file.read()

print(memory_read())