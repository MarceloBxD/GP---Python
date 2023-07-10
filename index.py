import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def salvar_senha(senha):
    with open('senha.txt', 'w') as arquivo:
        arquivo.write(senha)

def gerar_senha_callback():
    comprimento = int(comprimento_var.get())
    senha = gerar_senha(comprimento)
    salvar_senha(senha)
    messagebox.showinfo("Senha Gerada", f"Senha: {senha}\n\nA senha foi salva no arquivo 'senha.txt'")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Variável de controle para o comprimento da senha
comprimento_var = tk.StringVar()

# Rótulo e entrada para o comprimento da senha
comprimento_label = tk.Label(janela, text="Comprimento:")
comprimento_label.config(font=('Arial', 12, 'bold'))
comprimento_label.pack(padx=10, pady=10)
comprimento_entry = tk.Entry(janela, textvariable=comprimento_var)
comprimento_entry.pack(padx=10, pady=10)

# Botão para gerar a senha
gerar_button = tk.Button(janela, text="Gerar Senha", command=gerar_senha_callback)
gerar_button.config(width=15, height=1, padx=5, pady=2, bg="gray", fg="white")
gerar_button.pack()


# Execução da janela principal
janela.mainloop()