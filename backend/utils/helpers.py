
# Transforma lista de inteiros em string separada por vírgula
def lista_para_string(lista):
    return ",".join(str(i) for i in lista)

# Transforma string com inteiros separados por vírgula em lista de int
def string_para_lista(string):
    return [int(i) for i in string.split(",")]

# Exibe rota formatada
def formatar_rota(rota):
    return " → ".join(f"Ponto {i}" for i in rota)
