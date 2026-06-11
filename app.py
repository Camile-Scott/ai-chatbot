from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="sk-b4ea12a9c50e4704a15f2a7ad5010167",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    history.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="deepseek-v3",
        messages=history
    )
    
    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)