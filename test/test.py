# Это тестовый файл
import os
from os import path
import subprocess
import logging
import json

from httpx import patch
from system_file.tools import *
import lmstudio  as lms
from datetime import datetime

from pathlib import Path

# Абсолютный путь к файлу относительно текущей рабочей директории
print(write_file("app.log/../app.log","asdasda"))
