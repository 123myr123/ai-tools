# Инициализируем класс
import logging
logging.basicConfig(level=logging.INFO, filename="app.log",filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')
def question_user(question:str,option_1:str,option_2:str,option_3:str):
    """A tool for generating clarifying questions. Use it when there are multiple options and you need to select the right one—for instance, in design work. If you do not need three options, simply enter "0" in any of the fields, and that option will not be displayed."""
    logging.info("Создан вопрос к пользователю: " + question)
    logging.info(option_1)
    logging.info(option_2)
    logging.info(option_3)
    print("Вопрос модели к вам:")
    print(question)
    if not option_1 == "0":
        print("(1)"+option_1)
    if not option_2 == "0":
        print("(2)"+option_2)
    if not option_3 == "0":
        print("(3)"+option_3)
    user_input = input("Выберите вариант или впешите свой:   ")
    if user_input == "1":
        return "user Выбрал вариант "+option_1
    if user_input == "2":
            return "user Выбрал вариант "+option_2
    if user_input == "3":
            return "user Выбрал вариант "+option_3
    return "User не выбрал ничего и вписал свой вариант:    "+user_input

print(question_user("Абоьба?","1","2","0"))