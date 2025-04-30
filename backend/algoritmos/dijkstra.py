import heapq  # Usado para implementar fila de prioridade

def calcular_caminho(grafo, origem):
    # Inicializa as distâncias com infinito, exceto a origem
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0
    fila = [(0, origem)]  # Fila com a origem iniciando distância zero

    # Loop principal do algoritmo de Dijkstra
    while fila:
        dist, atual = heapq.heappop(fila)  # Pega o vértice mais próximo
        for vizinho, peso in grafo[atual]:  # Para cada vizinho do vértice atual
            nova_dist = dist + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila, (nova_dist, vizinho))  # Atualiza fila
    return distancias  # Retorna todas as distâncias mínimas desde a origem
