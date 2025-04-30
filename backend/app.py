from flask import Flask, request, jsonify
from roteirizador import gerar_rota_completa
from database.connection import conectar

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

@app.route("/historico", methods=["GET"])
def historico():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT bairro, rota, entrega_prioritaria, data_execucao FROM rotas ORDER BY id DESC")
    dados = cursor.fetchall()
    conn.close()

    historico = [
        {
            "bairro": row[0],
            "rota": [int(x) for x in row[1].split(",")],
            "entrega_prioritaria": row[2],
            "data_execucao": row[3]
        }
        for row in dados
    ]

    return jsonify(historico)

if __name__ == "__main__":
    app.run(debug=True)
