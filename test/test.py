# Это тестовый файл
import lmstudio as lms

# Create a chat with an initial system prompt.
model = lms.llm()
pyti = "system"
def memory_read():
    """reads the memory module"""
    y = ("system_file/profile/" +pyti)
    h = y + "/"
    pyti_config = h + "memory.txt"
    with open(pyti_config, "r", encoding='utf-8') as file:
        return file.read()
    
chat = lms.Chat.from_history({"messages": [
  { "role": "system", "content": "ты ии асистент все ответы должны быть на руском. Самое первое сообшение имееюшие тип memory:(текст) евляется твоей памятью между чатами" },
]})
chat.add_user_message("memory: " + memory_read())
# Build the chat context by adding messages of relevant types.
chat.add_user_message("Привет, скажи мне что у тебя в памяте")
result = model.respond(chat)
print(result)