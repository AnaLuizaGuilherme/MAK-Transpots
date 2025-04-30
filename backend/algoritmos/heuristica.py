# Define uma pontuação de prioridade para cada entrega
# A entrega com maior score será considerada a mais urgente

def calcular_prioridade(entrega):
    score = 0
    if entrega.get("tipo") == "urgente":
        score += 10
    if entrega.get("cliente_especial", False):
        score += 5
    if entrega.get("prazo_entrega", 999) < 30:
        score += 3
    return score
