import sqlite3

conexao = sqlite3.connect('clientes.db')
menssageiro = conexao.cursor()

menssageiro.execute('''CREATE TABLE clientes(
    Nome text,
    Sobrenome text,
    Email text,
    Telefone text
                   )
''')

conexao.commit()
conexao.close()
