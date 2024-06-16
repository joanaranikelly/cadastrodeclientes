import tkinter as tk
import sqlite3
import pandas as pd

# Configuração da janela principal
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("400x400")

# Função para criar a tabela se ela não existir
def criar_tabela():
    conexao = sqlite3.connect('clientes.db')
    menssageiro = conexao.cursor()
    menssageiro.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            nome TEXT,
                            sobrenome TEXT,
                            email TEXT,
                            telefone TEXT)''')
    conexao.commit()
    conexao.close()

# Função para cadastrar clientes
def cadastrar_clientes():
    conexao = sqlite3.connect('clientes.db')
    menssageiro = conexao.cursor()
    menssageiro.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
                        {
                            'nome': entry_nome.get(),
                            'sobrenome': entry_sobrenome.get(),
                            'email': entry_email.get(),
                            'telefone': entry_telefone.get()
                        })
    conexao.commit()
    conexao.close()
    entry_nome.delete(0, "end")
    entry_sobrenome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")

# Função para exportar clientes para um arquivo Excel
def exportar_clientes():
    conexao = sqlite3.connect('clientes.db')
    menssageiro = conexao.cursor()
    menssageiro.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = menssageiro.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['Nome', 'Sobrenome', 'Email', 'Telefone', 'Id_banco'])
    clientes_cadastrados.to_excel('clientes.xlsx', index=False)
    conexao.commit()
    conexao.close()

criar_tabela()

# Interface
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=35)
entry_email.grid(row=2, column=1, padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)

botao_cadastrar = tk.Button(janela, text='Cadastrar Cliente', command=cadastrar_clientes)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

botao_exportar = tk.Button(janela, text='Exportar para Excel', command=exportar_clientes)
botao_exportar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

# Inicia o loop da interface gráfica
janela.mainloop()
