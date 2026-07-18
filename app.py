import lmstudio as lms
from system_file.tools import *
import logging
from tools_app import chek_tools, profile_create, print_fragment
import platform
import datetime


print("Выберите что сделать:")
print("1 режим чата с ии")
print("2 создать новый профиль")
if int(input()) == 2:
   profile_create()
print("Выберите профиль из перечисленных")
for x in read_folder("system_file/profile"):
    print(x)
pyti = input("Выберите профиль: ")

def memory_write(content:str):
     """Writing to the memory module. Entries are preserved between sessions."""

     y = ("system_file/profile/" +pyti)
     pyti_config = y + "/memory.txt"
     file = open(pyti_config,'a', encoding='utf-8')
     file.write(content)
     file.close()
     return "The information has been recorded."

def memory_read():
    """reads the memory module"""
    y = ("system_file/profile/" +pyti)
    pyti_config = y + "/memory.txt"
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
    if config_file == "tools.json":
        tools = chek_tools(pyti_config)
        x = tools + [memory_read,memory_write]
        tools = x
        logging.info("инстурменты установлены")
        logging.info(tools)

SERVER_API_HOST = "localhost:1234"
lms.set_sync_api_timeout(720000)
lms.configure_default_client(SERVER_API_HOST)
model = lms.llm()
memory_message = memory_read() +">"
chat.add_user_message("<memory: " + memory_message)
with open('tools_config.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        chat.add_user_message("<workspace: ")
        for workspace in data["workspace"]:
            chat.add_user_message(workspace)
        chat.add_user_message(">")
system_ai = "<system:" + platform.system()
chat.add_user_message(system_ai + ">")
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
            local_now = datetime.datetime.now()
            x = "<time:" +local_now.strftime("%d/%m/%Y, %H:%M:%S")
            time_message = x + ">"
            chat.add_user_message(user_input + time_message)
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