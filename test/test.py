# Это тестовый файл
import os
import subprocess
name = "python3.13.exe test/test_copy.py"
t = subprocess.check_output(name, universal_newlines=True)
print(t)