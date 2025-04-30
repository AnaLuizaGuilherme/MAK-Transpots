import random

# Algoritmo genético que otimiza a sequência dos pontos de entrega
# baseado em uma matriz de distâncias e um ponto de partida

def algoritmo_genetico(pontos, matriz_distancia, geracoes=100, tamanho_pop=10):
    # Calcula a "aptidão" de uma rota (soma das distâncias entre os pontos na sequência)
    def fitness(caminho):
        return sum(matriz_distancia[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))

    # Gera um filho combinando dois pais
    def crossover(p1, p2):
        corte = random.randint(1, len(p1) - 2)
        filho = p1[:corte] + [x for x in p2 if x not in p1[:corte]]
        return filho

    # Troca dois pontos aleatórios no caminho
    def mutacao(caminho):
        i, j = random.sample(range(len(caminho)), 2)
        caminho[i], caminho[j] = caminho[j], caminho[i]
        return caminho

    # Cria população inicial
    populacao = [random.sample(pontos, len(pontos)) for _ in range(tamanho_pop)]

    # Evolui a população ao longo das gerações
    for _ in range(geracoes):
        populacao = sorted(populacao, key=fitness)
        nova_pop = populacao[:2]  # Mantém os dois melhores
        while len(nova_pop) < tamanho_pop:
            pai1, pai2 = random.choices(populacao[:5], k=2)
            filho = crossover(pai1, pai2)
            if random.random() < 0.3:
                filho = mutacao(filho)
            nova_pop.append(filho)
        populacao = nova_pop

    return populacao[0]  # Retorna a melhor rota (menor distância total)
