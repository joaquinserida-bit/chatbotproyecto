import os
from flask import Flask, request, jsonify
from openai import OpenAI

# Inicializar Flask
app = Flask(__name__)

# Configurar cliente de OpenAI
# Asegúrate de tener tu API key en una variable de entorno
client = OpenAI(api_key=os.environ.get("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"))

@app.route("/")
def home():
    return "✅ Chatbot médico sobre cáncer está funcionando en Render"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No se recibió ningún mensaje"}), 400

    try:
        # Llamada a OpenAI (modo asistente conversacional)
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # puedes usar gpt-4o si tu plan lo permite
            messages=[
                {"role": "system", "content": "Eres un asistente médico especializado en síntomas de cáncer. "
                                              "Responde de forma empática, detallada y clara. "
                                              "Aclara que no reemplazas a un médico real."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7
        )

        bot_reply = response.choices[0].message.content

        return jsonify({
            "user_message": user_message,
            "bot_reply": bot_reply
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

