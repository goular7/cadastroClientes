class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, cliente):
        if not root:
            return Node(cliente)
        elif cliente.cpf < root.cliente.cpf:
            root.left = self.insert(root.left, cliente)
        else:
            root.right = self.insert(root.right, cliente)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and cliente.cpf < root.left.cliente.cpf:
            return self.right_rotate(root)
        if balance < -1 and cliente.cpf > root.right.cliente.cpf:
            return self.left_rotate(root)
        if balance > 1 and cliente.cpf > root.left.cliente.cpf:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and cliente.cpf < root.right.cliente.cpf:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def pre_order(self, root):
        if not root:
            return
        print(f"{root.cliente.cpf}: {root.cliente.nome}")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def search(self, root, cpf, comparisons=0):
        if root is None or root.cliente.cpf == cpf:
            return root, comparisons
        comparisons += 1
        if cpf < root.cliente.cpf:
            return self.search(root.left, cpf, comparisons)
        return self.search(root.right, cpf, comparisons)
