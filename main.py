import tkinter as tk

# Lista para armazenar os dados salvos
dados_salvos = []

def salvar_dados(entry_nome, entry_idade, entry_salario):
    # Obtendo os dados dos campos de entrada
    nome = entry_nome.get()
    idade = entry_idade.get()
    salario = entry_salario.get()

    # Adicionando os dados à lista de dados salvos
    dados_salvos.append((nome, idade, salario))

    # Limpando os campos de entrada após salvar os dados
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_salario.delete(0, tk.END)

    # Mensagem de confirmação
    print("Dados salvos com sucesso!")

def consultar_dados():
    # Criando uma nova janela para exibir os dados salvos
    janela_consulta = tk.Toplevel()
    janela_consulta.title("Dados Salvos")

    # Criando um widget de texto para exibir os dados salvos
    texto_dados = tk.Text(janela_consulta)
    texto_dados.pack()

    # Preenchendo o widget de texto com os dados salvos
    for dado in dados_salvos:
        texto_dados.insert(tk.END, f"Nome: {dado[0]}, Idade: {dado[1]}, Salário: {dado[2]}\n")

def criar_janela():
    # Criando a janela principal
    janela = tk.Tk()
    janela.title("Cadastro de Dados")
    janela.configure(background='yellow')  # Definindo o fundo como amarelo

    # Campo de entrada para o nome
    lbl_nome = tk.Label(janela, text="Nome:")
    lbl_nome.pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    # Campo de entrada para a idade
    lbl_idade = tk.Label(janela, text="Idade:")
    lbl_idade.pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    # Campo de entrada para o salário
    lbl_salario = tk.Label(janela, text="Salário:")
    lbl_salario.pack()
    entry_salario = tk.Entry(janela)
    entry_salario.pack()

    # Botão para salvar os dados
    btn_salvar = tk.Button(janela, text="Salvar", command=lambda: salvar_dados(entry_nome, entry_idade, entry_salario))
    btn_salvar.pack(pady=5)

    # Botão para consultar os dados salvos
    btn_consultar = tk.Button(janela, text="Consultar Dados Salvos", command=consultar_dados)
    btn_consultar.pack(pady=5)

    # Rodar a janela
    janela.mainloop()

# Chamando a função para criar a janela
criar_janela()
