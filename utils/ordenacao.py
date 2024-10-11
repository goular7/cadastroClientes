def quicksort(clientes):
    if len(clientes) <= 1:
        return clientes
    pivot = clientes[len(clientes) // 2]
    left = [x for x in clientes if x.nome < pivot.nome]
    middle = [x for x in clientes if x.nome == pivot.nome]
    right = [x for x in clientes if x.nome > pivot.nome]
    return quicksort(left) + middle + quicksort(right)
