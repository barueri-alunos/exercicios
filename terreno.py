def area(larg, comp):
    area = larg * comp
    print(f'A área do terreno é de {area}m²')


print('Controle de terrenos')
print('-' * 20)
l = float(input('largura(m): '))
c = float(input('comprimento(m): '))
area(l, c)



