# Это тестовый файл
import os
import subprocess
import logging
import json
from system_file.tools import *
from pathlib import Path

print("Выберите профиль из перечисленых")
for x in read_folder("system_file/profile"):
    print(x)
pyti = input("Выберите профиль: ")
for config_file in read_folder("system_file/profile/" +pyti):
    y = ("system_file/profile/" +pyti)
    h = y + "/"
    pyti_config = h + config_file
    if config_file == "promt.txt":
        print(read_file(pyti_config)) 