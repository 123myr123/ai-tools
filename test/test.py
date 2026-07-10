from duckduckgo_search import DDGS
import logging

# Инициализируем класс
def search_duckduckgo(search:str,result:int):
    """Sends a request to the duckduckgo service. Result specifies the number of requests, 10 by default."""
    logging.info("Начат поиск по запросу: " +search)
    with DDGS() as ddgs:
        if not result <= 0 or result == None:
            logging.info("Поиск завершон")
            return ddgs.text(search, max_results= int(result))
        else:
            logging.info("Поиск завершон")
            return ddgs.text(search,max_results= 10)

print(search_duckduckgo("молоко",10))