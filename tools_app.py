import tools_config
import json

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