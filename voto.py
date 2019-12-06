def voto(ano):
    atual = 2019
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: voto opcional'
    else:
        return f'Com {idade} anos: voto obrigatório'

print(voto(2000))
