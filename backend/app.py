from flask import Flask, request, jsonify
from algoritmos.dijkstra import calcular_caminho

# Criação da aplicação Flask
app = Flask(__name__)

# Rota raiz para teste de funcionamento da API
@app.route("/")
def index():
    return "API de Roteirização Ativa!"

# Endpoint principal: recebe grafo e origem, retorna rota com Dijkstra
@app.route("/rota", methods=["POST"])
def rota():
    dados = request.get_json()  # Recebe JSON com grafo e ponto inicial
    grafo = dados["grafo"]
    origem = dados["origem"]
    resultado = calcular_caminho(grafo, origem)  # Executa algoritmo
    return jsonify({"rota": resultado})  # Retorna resultado como JSON

# Executa o servidor localmente em modo debug
if __name__ == "__main__":
    app.run(debug=True)
    