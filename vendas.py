salario = 2000

def ganhar_comissao(vendas):
    if vendas == 10:
        salario1 = salario + 200
        return f'Vc vai receber {salario1}'
    elif vendas > 10 and vendas < 25:
        salario2 = salario + 300 + (salario/2)
        return f'Vc vai receber {salario2}'
    elif vendas >= 25:
        salario3 = salario * 2
        return f'Vc vai receber {salario3} e será promovido'
    else:
        return 'Obrigado'

vendas = int(input('Quantas vendas vc teve?'))
print(ganhar_comissao(vendas))
