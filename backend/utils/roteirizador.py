
import json
from prioridade import encontrar_entrega_prioritaria
from genetico import algoritmo_genetico
from database.connection import salvar_rota

def carregar_entregas_do_bairro(bairro, caminho_json="data/lugares.json"):
    with open(caminho_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados.get(bairro, [])

def gerar_matriz_simulada(entregas):
    tamanho = len(entregas)
    return [[0 if i == j else round(1 + abs(i - j) * 0.7, 2) for j in range(tamanho)] for i in range(tamanho)]

# Gera uma rota para um caminhão a partir do galpão do "Centro"
def gerar_rota_para_caminhao(bairro, origem_bairro="Centro"):
    entregas = carregar_entregas_do_bairro(bairro)
    origem = carregar_entregas_do_bairro(origem_bairro)
    
    if not entregas or not origem:
        raise ValueError("Entregas ou galpão não encontrados.")

    if len(entregas) > 10:
        raise ValueError("Máximo de 10 entregas por caminhão permitido.")

    entregas_completas = origem[:1] + entregas  # galpão + entregas do bairro
    ids = list(range(len(entregas_completas)))
    
    matriz = gerar_matriz_simulada(entregas_completas)
    ponto_prioritario = encontrar_entrega_prioritaria(entregas_completas)
    
    ids.remove(ponto_prioritario)
    rota_ordenada = algoritmo_genetico(ids, matriz)
    rota_final = [ponto_prioritario] + rota_ordenada

    salvar_rota(bairro, rota_final, ponto_prioritario)
    return rota_final

# Recebe lista de 3 bairros e gera uma rota por caminhão
def gerar_rotas_multiplas(bairros):
    if len(bairros) != 3:
        raise ValueError("Devem ser fornecidos exatamente 3 bairros.")
    rotas = {}
    for bairro in bairros:
        rotas[bairro] = gerar_rota_para_caminhao(bairro)
    return rotas
