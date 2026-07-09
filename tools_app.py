import tools_config
import json
from system_file.tools import *

def chek_tools(pyti:str):
    with open(pyti, 'r', encoding='utf-8') as file: 
                tools = []
                data = json.load(file) 
                for data_info in data:
                        if data_info  == "create_file" and data[data_info] == 1:
                               x = tools + tools_config.tools_create_file      
                               tools = x                     
                        if data_info  == "create_folder" and data[data_info] == 1:
                             x =tools + tools_config.tools_create_folder
                             tools = x
                        if data_info  == "read_file" and data[data_info] == 1:
                             x =tools + tools_config.tools_read_file
                             tools = x
                        if data_info  == "read_folder" and data[data_info] == 1:
                             x =tools + tools_config.tools_read_folder
                             tools = x
                        if data_info  == "write_file" and data[data_info] == 1:
                             x =tools + tools_config.tools_write_file
                             tools = x
                        if data_info  == "run_command" and data[data_info] == 1:
                             x =tools + tools_config.tools_run_command
                             tools = x  
                        if data_info == "extract_text_from_url" and data[data_info] == 1:
                             x =tools + tools_config.tools_extract_text_from_url
                             tools = x       
                return tools
def profile_create():
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
      