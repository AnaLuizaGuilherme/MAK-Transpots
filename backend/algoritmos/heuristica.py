
from datetime import datetime

# Score agora baseado na data de entrega E tipo da entrega
def calcular_prioridade_data(entrega):
    hoje = datetime.now()
    data_entrega = datetime.strptime(entrega["data_entrega"], "%Y-%m-%d")
    dias_para_entrega = (data_entrega - hoje).days

    # Score base: quanto mais próxima a data, maior o score
    score = max(0, 30 - dias_para_entrega)

    # Pontos adicionais conforme o tipo da entrega
    tipo = entrega.get("tipo", "").lower()
    if tipo == "urgente":
        score += 10

    return score
