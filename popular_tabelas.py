from faker import Faker
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
fake = Faker()

# Popular a tabela usuarios
for _ in range(500):
    nome = fake.name()
    email = fake.email()
    cpf = fake.random_int(1000000000,9000000000)
    telefone = fake.random_int(1000000000,9000000000)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=100)
    e_instutor = fake.boolean(chance_of_getting_true=50)

    cursor.execute(
        f"INSERT INTO usuarios (nome, email, cpf, telefone, data_nascimento, e_instrutor) VALUES ('{nome}', '{email}', '{cpf}', '{telefone}', '{data_nascimento}', {e_instutor})"
    )

# Popular a tabela cursos 
for _ in range(10):
    nome = fake.word()
    descricao = fake.text()
    valor = fake.random_int(100, 1000)

    cursor.execute(
        f"INSERT INTO cursos (nome, descricao, valor) VALUES ('{nome}', '{descricao}', {valor})"
    )

# Popular a tabela transacoes
for _ in range(1000):
    id_usuario = fake.random_int(1, 30000)
    id_curso = fake.random_int(1, 40)
    metodo_pagamento = fake.random_element(elements=("cartao", "boleto", "pix"))
    descricao = fake.text()

    cursor.execute(
        f"INSERT INTO transacoes (id_usuario, id_curso, metodo_pagamento, descricao) VALUES ({id_usuario}, {id_curso}, '{metodo_pagamento}', '{descricao}')"
    )

# Confirmar as alterações no banco de dados
conexao.commit()

# Fechar a conexão e o cursor
cursor.close()
conexao.close()
