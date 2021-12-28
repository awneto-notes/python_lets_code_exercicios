def soma_listas(lista_a,lista_b):
    return([sum(item) for item in zip(lista_a,lista_b)])

print(soma_listas([1,2,3],[4,5,6]))
