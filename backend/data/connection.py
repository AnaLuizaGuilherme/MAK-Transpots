import sqlite3
from datetime import datetime

DB_PATH = "database/historico.db"

# Cria a conexão com o banco e inicializa a tabela se não existir
def conectar():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bairro TEXT NOT NULL,
            rota TEXT NOT NULL,
            entrega_prioritaria INTEGER NOT NULL,
            data_execucao TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn

# Salva os dados da rota calculada no banco
def salvar_rota(bairro, rota, entrega_prioritaria):
    conn = conectar()
    cursor = conn.cursor()
    data = datetime.now().isoformat()
    rota_str = ",".join(str(i) for i in rota)
    cursor.execute(
        "INSERT INTO rotas (bairro, rota, entrega_prioritaria, data_execucao) VALUES (?, ?, ?, ?)",
        (bairro, rota_str, entrega_prioritaria, data)
    )
    conn.commit()
    conn.close()
