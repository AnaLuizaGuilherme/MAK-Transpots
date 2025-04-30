import random

# Organiza a ordem dos pontos para menor custo total de percurso
def algoritmo_genetico(pontos, matriz_distancia, geracoes=50, tamanho_pop=6):
    def fitness(caminho):
        return sum(matriz_distancia[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1))

    def crossover(p1, p2):
        corte = random.randint(1, len(p1) - 2)
        return p1[:corte] + [x for x in p2 if x not in p1[:corte]]

    def mutacao(caminho):
        i, j = random.sample(range(len(caminho)), 2)
        caminho[i], caminho[j] = caminho[j], caminho[i]
        return caminho

    populacao = [random.sample(pontos, len(pontos)) for _ in range(tamanho_pop)]
    for _ in range(geracoes):
        populacao.sort(key=fitness)
        nova = populacao[:2]
        while len(nova) < tamanho_pop:
            p1, p2 = random.choices(populacao[:4], k=2)
            f = crossover(p1, p2)
            if random.random() < 0.3:
                f = mutacao(f)
            nova.append(f)
        populacao = nova
    return populacao[0]
