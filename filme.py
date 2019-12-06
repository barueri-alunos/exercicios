filmes = [
    {
        "titulo":"Invocação do Mal",
        "classificacao": 16
    },
    {
        "titulo":"Rei Leão",
        "classificacao": 12
    },
    {
        "titulo":"Lagoa Azul",
        "classificacao": 16
    },
    {
        "titulo":"Ninja Assassino",
        "classificacao": 18},
]

idade = int(input('qual a sua idade?'))
while idade < 0:
    print('Idade Inválida')
    idade = int(input('qual a sua idade de verdade?'))
for filme in filmes:
    if idade >= filme['classificacao']:
        print(f'Você pode assistir {filme["titulo"]}')
    elif idade < filme['classificacao']:
        print(f'Você não pode assistir {filme["titulo"]}')




