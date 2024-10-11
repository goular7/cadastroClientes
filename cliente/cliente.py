class Cliente:
    def __init__(self, nome, data_nascimento, telefone, email, endereco, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome}, {self.data_nascimento}, {self.telefone}, {self.email}, {self.endereco}, {self.cpf}"
