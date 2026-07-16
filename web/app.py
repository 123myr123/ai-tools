from flask import Flask, request, jsonify, render_template
import lmstudio as lms
app = Flask(__name__)

model = lms.llm()
chat_ai = lms.Chat()
def ai_chat(text:str):
    chat_ai.add_user_message(text)
    ai_text = str(model.respond(chat_ai))
    return ai_text
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    text= ai_chat(user_message)
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

if __name__ == '__main__':
    app.run(debug=True)