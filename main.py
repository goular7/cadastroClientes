from cliente.cliente import Cliente
from cliente.cliente_db import ClienteDB

cliente_db = ClienteDB()

def main():
    while True:
        print("\n1. Cadastrar Cliente\n2. Buscar Cliente por CPF\n3. Listar Clientes (por CPF)\n4. Listar Clientes (por Nome)\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            buscar_cliente_por_cpf()
        elif opcao == "3":
            listar_clientes()
        elif opcao == "4":
            listar_clientes_ordenados_por_nome()
        elif opcao == "5":
            cliente_db.fechar_conexao()
            break
        else:
            print("Opção inválida")

def cadastrar_cliente():
    nome = input("Nome Completo: ")
    data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")

    cliente = Cliente(nome, data_nascimento, telefone, email, endereco, cpf)
    cliente_db.cadastrar_cliente(cliente)

def buscar_cliente_por_cpf():
    cpf = input("Digite o CPF para busca: ")
    cliente = cliente_db.buscar_cliente_por_cpf(cpf)
    if cliente:
        print(f"Cliente encontrado: {cliente}")
    else:
        print("Cliente não encontrado")

def listar_clientes():
    clientes = cliente_db.listar_clientes()
    for cliente in clientes:
        print(cliente)

def listar_clientes_ordenados_por_nome():
    clientes = cliente_db.listar_clientes_ordenados_por_nome()
    for cliente in clientes:
        print(cliente)

if __name__ == "__main__":
    main()
