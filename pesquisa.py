def pesquisar(lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return None

L=[10, 20, 25, 30]
print(pesquisar(L, 25))
print(pesquisar(L, 27))


