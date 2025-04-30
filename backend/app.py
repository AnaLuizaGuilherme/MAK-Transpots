
from flask import Flask, request, jsonify
from roteirizador import gerar_rota_completa

app = Flask(__name__)

@app.route("/rota", methods=["POST"])
def rota():
    dados = request.get_json()
    bairro = dados.get("bairro")

    if not bairro:
        return jsonify({"erro": "bairro não informado"}), 400

    try:
        rota_final = gerar_rota_completa(bairro)
        return jsonify({"bairro": bairro, "rota": rota_final})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
