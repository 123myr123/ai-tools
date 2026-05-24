from pathlib import Path
import lmstudio as lms
import os

def run_comand(name:str):
    """executes a system command and returns its exit code(if successful 0)"""
    print("вызвон инструмент run_comand")
    print("ии хочет вызвать команду " +name)
    if input("Y/N") == "Y":
        command = os.system(name)
        if command == 0:
            return "command called successfully"
        else:
            return "command call failed"
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

tools = [create_file,read_file,write_file,read_folder,create_folder,run_comand]
SERVER_API_HOST = "localhost:1234"
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm()
chat = lms.Chat("ты ии ассистент. Ответы на вопросы пользователя всегда должны быть на русском. ТЕБЕ ЗАПРЕШЕНО КАК ЛИБО МЕНЯТЬ КОД В app.py.")
while True:
    mode = int(input("Выберите режим: 1 инструменты, 2 Фото     "))
    if mode == 1:
        while True:
    
            try:
                user_input = input("сообщение:")
            except EOFError:
                print()
                break
            if not user_input:
                break
            chat.add_user_message(user_input)
            print("Bot: ", end="", flush=True)
            model.act(
                chat,
                tools,
                on_message=chat.append,
                on_prediction_fragment=print_fragment,
            )
            print()
    else:
        image_path = input("Введите путь к фото:") # Replace with the path to your image
        image_handle = lms.prepare_image(image_path)
        user_input = input("cообщение:")
        chat.add_user_message(user_input, images=[image_handle])
        prediction_stream = model.respond_stream(
            chat,
            on_message=chat.append,
        )
        print("Bot: ", end="", flush=True)
        for fragment in prediction_stream:
            print(fragment.content, end="", flush=True)
        print()