from pathlib import Path
import lmstudio as lms
def multiply(a: float, b: float) -> float:
    """Given two numbers a and b. Returns the product of them."""
    return a * b
def create_file(name: str, content: str):
    """Create a file with the given name and content."""
    dest_path = Path(name)
    if dest_path.exists():
        return "Error: File already exists."
    try:
        dest_path.write_text(content, encoding="utf-8")
    except Exception as exc:
        return "Error: {exc!r}"
    return "File created."
def print_fragment(fragment, round_index=0):
    # .act() supplies the round index as the second parameter
    # Setting a default value means the callback is also
    # compatible with .complete() and .respond().
    print(fragment.content, end="", flush=True)
model = lms.llm()
chat = lms.Chat("ты ии ассистент. Ответы на вопросы пользователя всегда должны быть на русском")
mode = int(input("Выберите режим 1 инструменты. 2 Фото"))
while True:
    mode = int(input("Выберите режим 1 инструменты. 2 Фото"))
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
                [create_file, multiply],
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