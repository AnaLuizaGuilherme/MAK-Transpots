from datetime import datetime

# Calcula score com base na proximidade da data de entrega
def calcular_prioridade_data(entrega):
    hoje = datetime.now()
    data_entrega = datetime.strptime(entrega["data_entrega"], "%Y-%m-%d")
    dias_para_entrega = (data_entrega - hoje).days
    score = max(0, 30 - dias_para_entrega)  # Quanto mais perto, maior o score
    return score
