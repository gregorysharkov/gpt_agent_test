from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    ai_message = response.choices[0].message["content"]
    return jsonify({"message": ai_message})


if __name__ == "__main__":
    app.run(debug=True)
