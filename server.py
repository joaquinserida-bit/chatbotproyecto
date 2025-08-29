from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor Flask corriendo"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    # Aquí tu lógica con OpenAI o reglas
    return jsonify({"bot_reply": f"Recibí tu mensaje: {user_input}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

