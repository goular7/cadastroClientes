import mysql.connector

class ClienteDB:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1970",
            database="cliente_cadastro"
        )
        self.cursor = self.conexao.cursor()

    def cadastrar_cliente(self, cliente):
        sql = "INSERT INTO clientes (nome, data_nascimento, telefone, email, endereco, cpf) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (cliente.nome, cliente.data_nascimento, cliente.telefone, cliente.email, cliente.endereco, cliente.cpf)
        self.cursor.execute(sql, values)
        self.conexao.commit()
        print(f"Cliente {cliente.nome} cadastrado com sucesso.")

    def buscar_cliente_por_cpf(self, cpf):
        sql = "SELECT * FROM clientes WHERE cpf = %s"
        self.cursor.execute(sql, (cpf,))
        cliente = self.cursor.fetchone()
        return cliente

    def listar_clientes(self):
        sql = "SELECT * FROM clientes"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def listar_clientes_ordenados_por_nome(self):
        sql = "SELECT * FROM clientes ORDER BY nome"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
