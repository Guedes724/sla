
lista1 = input("Digite os números da lista 1: ").split()
lista2 = input("Digite os números da lista 2: ").split()

lista1 = [int(x) for x in lista1]
lista2 = [int(x) for x in lista2]

lista_uni = list(set(lista1 + lista2))

print("Lista unificada:", *lista_uni)
