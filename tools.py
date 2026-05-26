from pathlib import Path
import os
import subprocess

def run_comand(name:str):
    """Executes the command specified in the command name. It waits for the command to complete and then displays the result. If input is required during the call, the user enters it."""
    print("вызвон инструмент run_comand")
    print("ии хочет вызвать команду " +name)
    if input("Y/N") == "Y":
        command = subprocess.check_output(name, universal_newlines=True)
        print(command)
        return command
    else:
        return "denied by user"
def create_folder(name:str):
    """creates a directory without intermediate directories"""
    folder = os.mkdir(name, mode=0o777,  dir_fd=None)
    print("вызвон инструмент create_folder")
    print()
    if folder == None:
        return "folder created successfully"
    else:
        return "The folder was not created, it already exists."
def read_folder(name: str):
    """List of files and directories in a folder. The dot (.) symbol shows directories and files in the root folder."""
    print("вызвон инструмент read_folder")
    print()
    return (os.listdir(path= name))
def write_file(name: str, content: str):
    """open for writing, file contents are deleted, if the file does not exist, a new one is created"""
    file = open(name,'w', encoding='utf-8')
    file.write(content)
    file.close
    print("вызвон инструмент write_file")
    print()
    return "information recorded"
def read_file(name: str):
    """Read the specified file. Returns the file contents."""
    print("вызвон инструмент read_file")
    print()
    file = open(name)
    return file.read()
def create_file(name: str, content: str):
    """Create a file with the given name and content."""
    dest_path = Path(name)
    if dest_path.exists():
        return "Error: File already exists."
    try:
        dest_path.write_text(content, encoding="utf-8")
    except Exception as exc:
        return "Error: {exc!r}"
    print("вызвон инструмент create_file")
    print()
    return "File created."
def print_fragment(fragment, round_index=0):
    # .act() supplies the round index as the second parameter
    # Setting a default value means the callback is also
    # compatible with .complete() and .respond().
    print(fragment.content, end="", flush=True)