
from algoritmos.heuristica import calcular_prioridade
from algoritmos.genetico import algoritmo_genetico
from algoritmos.dijkstra import calcular_caminho

# Define o ponto inicial com base na heurística de prioridade
def encontrar_entrega_prioritaria(entregas):
    melhor_score = -1
    entrega_prioritaria = None
    for entrega in entregas:
        score = calcular_prioridade(entrega)
        if score > melhor_score:
            melhor_score = score
            entrega_prioritaria = entrega
    return entrega_prioritaria["id"]

# Otimiza a ordem das entregas começando pelo ponto prioritário
def gerar_roteiro_otimizado(entregas, matriz_distancia):
    pontos = [entrega["id"] for entrega in entregas]
    ponto_prioritario = encontrar_entrega_prioritaria(entregas)

    pontos_sem_inicio = [p for p in pontos if p != ponto_prioritario]
    rota_ordenada = algoritmo_genetico(pontos_sem_inicio, matriz_distancia)
    rota_final = [ponto_prioritario] + rota_ordenada

    return rota_final

# Gera um dicionário com todas as distâncias entre os pontos do caminho final
def calcular_rotas_completas(rota_final, grafo):
    distancias_totais = {}
    for i in range(len(rota_final) - 1):
        origem = rota_final[i]
        destino = rota_final[i + 1]
        distancias = calcular_caminho(grafo, origem)
        distancias_totais[f"{origem}-{destino}"] = distancias[destino]
    return distancias_totais
