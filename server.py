from flask import Flask, request, jsonify
import openai

# Configuración de la API Key (pon la tuya aquí)
openai.api_key = "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"

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # puedes usar gpt-4 si tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente médico educativo que aclara síntomas y posibles causas, pero siempre recuerda que NO reemplazas al médico."},
                {"role": "user", "content": user_msg}
            ],
            max_tokens=200
        )

        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"⚠️ Error en el servidor: {str(e)}"})
    

if __name__ == "__main__":
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

