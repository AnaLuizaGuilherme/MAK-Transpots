
# 🚚 Sistema de Roteirização de Entregas com Flask e React Native

Este projeto simula um sistema de otimização de rotas para entregas urbanas. Utiliza algoritmos de inteligência artificial e heurísticas para gerar a rota mais eficiente a partir de um galpão central (bairro "Centro") para até 3 caminhões de entrega.

---

## 📌 Objetivo

Calcular a **menor rota possível** para pontos de entrega pré-estabelecidos, usando:

- Algoritmo de Dijkstra (obrigatório)
- Heurística para identificar entregas prioritárias por tipo e data
- Algoritmo Genético para otimização de sequência

Limite de **10 entregas por caminhão**, cada um atendendo um bairro diferente.

---

## 🧠 Arquitetura do Sistema

- **Frontend:** React Native (consome a API)
- **Backend:** Flask (Python)
- **Dados:** JSON para simulação, SQLite para histórico
- **Algoritmos:** Heurística, Genético, Dijkstra

**Diagrama da Arquitetura!**

![image](https://github.com/user-attachments/assets/7e384fb9-2870-448a-b5ad-f6a081e6b740)


---

## 🗃️ Estrutura do Projeto

```
/backend
├── app.py                   # API principal
├── roteirizador.py          # Geração de rotas (3 caminhões)
├── heuristica.py            # Score por data e tipo
├── prioridade.py            # Seleciona entrega prioritária
├── genetico.py              # Otimiza ordem de entrega
├── connection.py            # Banco SQLite
├── helpers.py               # Funções auxiliares
├── json_loader.py           # Carregamento de entregas por bairro
├── data/
│   └── lugares.json         # Dados simulados das entregas
├── database/
│   └── historico.db         # Histórico das rotas
└── requirements.txt
```

---

## 🚀 Como Executar

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```
3. Inicie o servidor:
```bash
python app.py
```

---

## 🔗 Endpoints da API

### `POST /rota`
Calcula a rota para até 3 caminhões.
```json
{
  "bairros": ["Jardim São Paulo", "Braz Cubas", "Vila Oliveira"]
}
```

### `GET /historico`
Retorna o histórico das rotas geradas.

---

## 📍 Considerações

- O ponto inicial de todas as rotas é sempre o galpão localizado no bairro **"Centro"**.
- Cada rota atende **um único bairro**, com no máximo 10 entregas.
- As entregas são simuladas com dados em JSON.

---

## 📄 Licença

Este projeto é de uso educacional. Desenvolvido por Ana Luiza Guilherme, Kayky Oliveira e Murillo Rodrigues com orientação da professora Andrea Ono Sakai e suporte do ChatGPT.
