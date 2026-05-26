from pathlib import Path
import lmstudio as lms
import os
import subprocess
from tools import *

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