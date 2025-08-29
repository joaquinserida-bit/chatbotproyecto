import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal para probar que funciona
@app.route("/")
def home():
    return "✅ Servidor Flask funcionando en Render"

# Ruta de ejemplo tipo API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # Respuesta de prueba (más adelante la cambiamos por el chatbot real)
    response = {
        "user_message": user_message,
        "reply": f"Recibí tu mensaje: {user_message}"
    }
    return jsonify(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port)

