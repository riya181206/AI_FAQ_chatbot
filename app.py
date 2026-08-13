from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot
import os

app = Flask(__name__)

chatbot = FAQChatbot()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    answer = chatbot.get_answer(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)