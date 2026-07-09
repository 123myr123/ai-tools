"""
Скрипт для взаимодействия с LM Studio ИИ с озвучкой ответов и распознаванием речи
Автор: AI-ассистент

Функционал:
- Запись звука по нажатию Enter (один раз на запись)
- После завершения ждёт повторного нажатия Enter для новой записи
- Озвучивание ответов ИИ
- Удаление текста до < перед отправке в модель
"""

import lmstudio as lms
import pyttsx3
import speech_recognition as sr
import keyboard


class VoiceAssist:
    def __init__(self):
        # Инициализация движка
        self.model = lms.llm()
        
        # Инициализация синтезатора речи (озвучивание)
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        russian_voices = [v for v in voices if 'russian' in v.name.lower()]
        if russian_voices:
            self.engine.setProperty('voice', russian_voices[0].id)
        
        # Создание диалога с ИИ
        self.chat = lms.Chat("Ты ИИ-ассистент. Все ответы должны быть на русском языке.Тебе запрешено использовать смайлики. Если ты получил не понятное слово то попроси пользователя повторить что он сказал.")
        
        print("=" * 50)
        print("Диалог с ИИ запущен")
        print("=" * 50)

    def listen(self, recognizer=None):
        """Запись звука по запросу (ждёт Enter для старта)"""
        # Если recognizer не передан, создаём новый
        if recognizer is None:
            r = sr.Recognizer()
            r.energy_threshold = 300
            with sr.Microphone() as source:
                print("Нажмите Enter для новой записи или введите exit чтобы закончить.")
                
                print("🎤 Запись началась. Говорите...")
                keyboard.wait('q')
                # Сброс шума окружения (важно для стабильной работы)
                r.adjust_for_ambient_noise(source, duration=1)
                
                audio = r.listen(source, timeout=50)  # Максимум 50 секунд записи
                return audio

    def recognize(self, text):
        """Распознавание текста из аудио (вызывается внутри listen())"""
        # Распознавание речи с помощью Google Speech API
        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            
            # Вывод полного текста в консоль
            print(f"📝 Вы сказали: {text}")
            
            return text
            
        except sr.UnknownValueError:
            print("❌ Не удалось распознать речь. Попробуйте снова.")
            return None
        except sr.RequestError as e:
            print(f"⚠️ Ошибка сервиса распознавания речи: {e}")
            return None

    def clean_text(self, text):
        """Очистка текста от маркера <"""
        # Удаляем всё, что идёт после < (включая сам <)
        cleaned = text.split('<')[0] if '<' in text else text
        print(f"📤 Отправляется в ИИ: {cleaned}")
        return cleaned

    def process(self):
        """Основной цикл обработки"""
        r = sr.Recognizer()
        r.energy_threshold = 300
        
        while True:
            try:
                # 1. Запись звука (с тем же recognizer)
                audio = self.listen(r)
                
                # Если запись не состоялась, ждём повторного Enter
                if not audio:
                    print("⏸️ Ожидание новой записи... Нажмите Enter")
                    input("Нажмите Enter для продолжения или 'exit' чтобы завершить:")
                    continue
                
                # 2. Распознавание текста (с тем же recognizer и аудио)
                text = r.recognize_google(audio, language="ru-RU")
                
                print(f"📝 Вы сказали: {text}")
                
                # Если распознавание не удалось, ждём повторного Enter
                if not text or text is None:
                    print("❌ Не удалось распознать речь. Повторите попытку.")
                    input("Нажмите Enter для продолжения или 'exit' чтобы завершить:")
                    continue
                
                # 3. Очистка текста (удаляем маркер <)
                clean_text = self.clean_text(text)
                
                # 4. Проверка на выход из программы
                if clean_text.lower() in ["exit", "quit", "выход"]:
                    print("Завершение диалога...")
                    break
                
                # 5. Отправка текста в ИИ (уже очищенного)
                self.chat.add_user_message(clean_text)
                
                # 6. Получение ответа от ИИ
                prediction = self.model.respond(self.chat)
                
                # 7. Озвучивание ответа ИИ
                print(f"🤖 Ответ ИИ: {prediction}")
                self.engine.say(str(prediction))
                self.engine.runAndWait()
            
            except KeyboardInterrupt:
                print("\n\n⛔ Программа остановлена по кнопке (Ctrl+C)")
                break
            except Exception as e:
                print(f"\n❌ Ошибка: {e}")
                continue

    def run(self):
        """Запуск диалога"""
        try:
            self.process()
        except Exception as e:
            print(f"Критическая ошибка: {e}")


# Основной запуск программы
if __name__ == "__main__":
    assist = VoiceAssist()
    assist.run()
