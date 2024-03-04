import mysql.connector

# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="test",
    password="test",
    database="test",
    auth_plugin='mysql_native_password'
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Extrair dados da tabela usuarios
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

with open("lake/usuarios.csv", "w") as arquivo:
    arquivo.write("id,nome,email,cpf,telefone,ano_nascimento,mes_nascimento,dia_nascimento,e_instrutor\n")
    for usuario in usuarios:
        usuario = str(usuario).replace("(", "").replace(")", "").replace("datetime.date", "").replace("'", "")
        arquivo.write(usuario + "\n")

# Extrair dados da tabela cursos
cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()

with open("lake/cursos.csv", "w") as arquivo:
    arquivo.write("id,nome,descricao,valor\n")
    for curso in cursos:
        curso = str(curso).replace("(", "").replace(")", "").replace("'", "").replace("Decimal", "")
        arquivo.write(curso + "\n")

# Extrair dados da tabela transacoes
cursor.execute("SELECT * FROM transacoes")
transacoes = cursor.fetchall()

with open("lake/transacoes.csv", "w") as arquivo:
    arquivo.write("id,id_usuario,id_curso,metodo_pagamento,descricao\n")
    for transacao in transacoes:
        transacao = str(transacao).replace("(", "").replace(")", "").replace("'", "")
        arquivo.write(transacao + "\n")