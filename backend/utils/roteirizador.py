
import json
from prioridade import encontrar_entrega_prioritaria
from genetico import algoritmo_genetico

# Lê o JSON e retorna as entregas de um bairro específico
def carregar_entregas_do_bairro(bairro, caminho_json="data/lugares.json"):
    with open(caminho_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados.get(bairro, [])

# Gera matriz simulada de distâncias para testes
def gerar_matriz_simulada(entregas):
    tamanho = len(entregas)
    return [[0 if i == j else round(1 + abs(i - j) * 0.7, 2) for j in range(tamanho)] for i in range(tamanho)]

# Gera rota com heurística e genético com base no bairro escolhido
def gerar_rota_completa(bairro):
    entregas = carregar_entregas_do_bairro(bairro)
    if not entregas:
        raise ValueError("Nenhuma entrega encontrada para o bairro informado.")
    ids = list(range(len(entregas)))
    matriz = gerar_matriz_simulada(entregas)
    ponto_prioritario = encontrar_entrega_prioritaria(entregas)
    ids.remove(ponto_prioritario)
    rota_ordenada = algoritmo_genetico(ids, matriz)
    rota_final = [ponto_prioritario] + rota_ordenada
    return rota_final
