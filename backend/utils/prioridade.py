from heuristica import calcular_prioridade_data

# Recebe uma lista de entregas e retorna o ID da mais prioritária
def encontrar_entrega_prioritaria(entregas):
    melhor_score = -1
    entrega_prioritaria = None
    for entrega in entregas:
        score = calcular_prioridade_data(entrega)
        if score > melhor_score:
            melhor_score = score
            entrega_prioritaria = entrega
    return entrega_prioritaria["id"]
