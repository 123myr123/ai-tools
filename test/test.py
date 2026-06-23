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
print(create_folder("test"))