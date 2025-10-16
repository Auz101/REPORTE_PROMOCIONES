from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "ok", "message": "API de reportes activa ✅"})

@app.route("/generar_reporte", methods=["POST"])
def generar_reporte():
    data = request.get_json()
    email = data.get("email")
    cod_promocion = data.get("cod_promocion")
    return jsonify({
        "status": "recibido",
        "email": email,
        "cod_promocion": cod_promocion
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
