from asyncio import tools
import lmstudio as lms
from system_file.tools import *
import logging
from tools_app import chek_tools

def print_fragment(fragment, round_index=0):
    # .act() supplies the round index as the second parameter
    # Setting a default value means the callback is also
    # compatible with .complete() and .respond().
    print(fragment.content, end="", flush=True)

print("Выберите что сделать:")
print("1 режим чата с ии")
print("2 создать новый профиль")
if int(input()) == 2:
    print("Выберите действие:")
    print("1 Создать новый профиль")
    print("2 Скопировать старый")
    print("3 скопировать старый(без памяти)")
    user_answer = int(input())
    if user_answer == 1:
            print("1 Создать новый промт")
            print("2 Скопировать старый из другого профиля")
            print("3 не создовать промт")
            user_answer = int(input())
            if user_answer == 1:
                new_profile = "system_file/profile/" + input("Введите имя профиля:")
                create_folder(new_profile)
                new_file = new_profile + "/promt.txt"
                create_file(new_file,str(input("ведите системный промт")))
                new_file = new_profile + "/memory.txt"
                create_file(new_file,"")
                new_file = new_profile + "/tools.json"
                create_file(new_file,read_file("system_file/copy.json"))
            elif user_answer == 2:
                new_profile = "system_file/profile/" + input("В ведите име профиля:")
                for x in read_folder("system_file/profile"):
                    print(x)
                user_answer ="system_file/profile/"+ str(input("Выберите профиль с которого скопировать: "))
                new_file = new_profile + "/promt.txt"
                print("Выберите профиль из перечисленых")
                create_folder(new_profile)
                create_file(new_file,read_file(user_answer + "/promt.txt"))
                new_file = new_profile + "/memory.txt"
                create_file(new_file,"")
                new_file = new_profile + "/tools.json"
                create_file(new_file,read_file("system_file/copy.json"))
            elif user_answer == 3:
                new_profile = "system_file/profile/" + input("В ведите име профиля:")
                create_folder(new_profile)
                new_file = new_profile + "/memory.txt"
                create_file(new_file,"")
                new_file = new_profile + "/tools.json"
                create_file(new_file,read_file("system_file/copy.json"))
    elif user_answer == 2:
        old_profile = "system_file/profile/" + input("Введите имя старого профиля:")
        new_profile = "system_file/profile/" + input("Введите имя нового профиля:")
        create_folder(new_profile)
        new_file = new_profile + "/promt.txt"
        old_file = old_profile + "/promt.txt"
        create_file(new_file,read_file(old_file))
        new_file = new_profile + "/memory.txt"
        old_file = old_profile + "/memory.txt"
        create_file(new_file,read_file(old_file))
        new_file = new_profile + "/tools.json"
        old_file = old_profile + "/tools.json"
        create_file(new_file,read_file(old_file))
    elif user_answer == 3:
        old_profile = "system_file/profile/" + input("Введите имя старого профиля:")
        new_profile = "system_file/profile/" + input("Введите имя нового профиля:")
        create_folder(new_profile)
        new_file = new_profile + "/promt.txt"
        old_file = old_profile + "/promt.txt"
        create_file(new_file,read_file(old_file))
        new_file = new_profile + "/memory.txt"
        create_file(new_file,"")
        new_file = new_profile + "/tools.json"
        old_file = old_profile + "/tools.json"
        create_file(new_file,read_file(old_file))

print("Выберите профиль из перечисленных")
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
     file.close()
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
    if config_file == "tools.json":
        logging.info("инстурменты установлены")
        tools = chek_tools(pyti_config)
        x = tools + [memory_read,memory_write]
        tools = x

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