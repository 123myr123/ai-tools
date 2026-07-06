# Это тестовый файл
import requests
from bs4 import BeautifulSoup



url = input("Вставте ссылку: ")
response = requests.get(url)
response.raise_for_status()
print(response.text)
soup = BeautifulSoup(response.text, 'lxml')
text = soup.get_text()
print(text)