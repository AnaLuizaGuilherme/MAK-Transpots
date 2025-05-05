
import tkinter as tk
from tkinter import ttk, messagebox
import requests

class AdminApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Painel Administrativo de Entregas")
        self.master.geometry("800x500")

        # Bairros para simulação
        self.bairros = ["Jardim São Paulo", "Braz Cubas", "Vila Oliveira"]
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Painel Administrativo", font=("Arial", 16)).pack(pady=10)

        ttk.Button(self.master, text="Simular Rotas (3 caminhões)", command=self.simular_rotas).pack(pady=5)
        ttk.Button(self.master, text="Visualizar Histórico", command=self.ver_historico).pack(pady=5)

        self.output = tk.Text(self.master, height=20, width=100)
        self.output.pack(pady=10)

    def simular_rotas(self):
        try:
            response = requests.post("http://127.0.0.1:5000/rota", json={"bairros": self.bairros})
            if response.status_code == 200:
                rotas = response.json()
                self.output.delete("1.0", tk.END)
                for bairro, rota in rotas.items():
                    self.output.insert(tk.END, f"Bairro: {bairro}\nRota: {rota}\n\n")
            else:
                messagebox.showerror("Erro", "Erro ao calcular rotas.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def ver_historico(self):
        try:
            response = requests.get("http://127.0.0.1:5000/historico")
            if response.status_code == 200:
                historico = response.json()
                self.output.delete("1.0", tk.END)
                for item in historico:
                    self.output.insert(tk.END, f"{item['data_execucao']} - {item['bairro']} - Prioritária: {item['entrega_prioritaria']}\nRota: {item['rota']}\n\n")
            else:
                messagebox.showerror("Erro", "Erro ao carregar histórico.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminApp(root)
    root.mainloop()
