import lmstudio as lms
from system_file.tools import *
import logging


def print_fragment(fragment, round_index=0):
    # .act() supplies the round index as the second parameter
    # Setting a default value means the callback is also
    # compatible with .complete() and .respond().
    print(fragment.content, end="", flush=True)

print("Выберите профиль из перечисленых")
for x in read_folder("system_file/profile"):
    print(x)
pyti = input("Выберите профиль: ")

def memory_write(content:str):
     """Writing to the memory module. Entries are preserved between sessions."""

     y = ("system_file/profile/" +pyti)
     h = y + "/"
     pyti_config = h + "memory.txt"
     file = open(pyti_config,'a', encoding='utf-8')
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


logging.info("выбран профиль " +pyti)
for config_file in read_folder("system_file/profile/" +pyti):
    y = ("system_file/profile/" +pyti)
    h = y + "/"
    pyti_config = h + config_file
    if config_file == "promt.txt":
        chat = lms.Chat(read_file(pyti_config))
        logging.info("загружен системный промт")
    if read_file(pyti_config) == "yes":
        tools = [create_file,read_file,write_file,read_folder,create_folder,run_comand,memory_read,memory_write]
        logging.info("загружены инструменты и модуль памяти")
    elif read_file(pyti_config) == "memory":
        tools = [memory_read,memory_write]
        logging.info("загружена только работа с памятью")
    elif read_file(pyti_config) =="tools":
        tools = [create_file,read_file,write_file,read_folder,create_folder,run_comand]
        logging.info("загружены только инструменты")
SERVER_API_HOST = "localhost:1234"
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm()
while True:
    mode = int(input("Выберите режим: 1 инструменты, 2 Фото     "))
    if mode == 1:
        logging.info("Выброн режим работы с инструментами")
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
    elif mode == 2:
        logging.info("загружен режим фото")
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