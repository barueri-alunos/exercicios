cont = 2

def contador(inicio, fim, passo):
    cont = inicio
    while cont <= fim:
        print(f'{cont}', end=' ')
        cont += passo
    print('fim!')

contador(1, 10, 1)
contador(1, 40, 2)
print(cont)

