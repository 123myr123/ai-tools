from flask import Flask, request, jsonify, render_template
import lmstudio as lms
import json
app = Flask(__name__)

model = lms.llm()
ai = {
     'messages': [ 
           {'role': 'system', 'content': 'Я — AI-ассистент. Все ответы должны быть на русском'}, 
     ]
}
with open("histori.json", "w",encoding='utf-8') as f:
        json.dump(ai, f)
def ai_chat(text:str):
    with open('histori.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        chat_ai = lms.Chat.from_history(data)
        file.close
    chat_ai.add_user_message(text)
    ai_text = str(model.respond(chat_ai))
    new_message = {'role': 'user', 'content': text}
    data['messages'].append(new_message)
    new_message = {'role': 'assistant', 'content': ai_text}
    data['messages'].append(new_message)
    with open("histori.json", "w",encoding='utf-8') as f:
        json.dump(data, f)
    return ai_text
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    text= ai_chat(user_message)
    if not text.find('<channel|>') == -1:
        start =text.find('<|channel>')
        end =text.find('<channel|>')
        result = text[start + 1:end]
        # Тестовые данные – заполняем все поля
        thinking_text = (
            f"{result}"
        )

        response_text = (
            f"{text[end:]}"
        )

        return jsonify({
            "thinking": thinking_text,
            "response": response_text
        })
    else:
            response_text = (
                     f"{text}"
                 )
            return jsonify({
                "response": response_text
            })
if __name__ == '__main__':
    app.run(debug=True)