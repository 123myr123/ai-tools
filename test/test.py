import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    """
    Извлекает и возвращает чистый текстовый контент с указанного URL.
    """
    try:
        # 1. Отправляем GET-запрос
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # выбросит исключение при HTTP-ошибке

        # 2. Создаём объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # 3. Удаляем теги <script> и <style>, чтобы не захватывать код
        for element in soup(["script", "style"]):
            element.decompose()

        # 4. Извлекаем весь текст с разделителем по строкам
        raw_text = soup.get_text(separator='\n', strip=True)

        # 5. Очищаем текст от пустых строк
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        clean_text = '\n'.join(lines)

        return clean_text

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    return None

if __name__ == "__main__":
    url = input("Введите URL сайта: ")
    text = extract_text_from_url(url)

    if text:
        print("\n--- Извлечённый текст ---\n")
        print(text)
    else:
        print("Не удалось получить текст.")