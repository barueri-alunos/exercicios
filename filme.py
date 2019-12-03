
filmes = [
    {
        "titulo":"Invocação do Mal",
        "classificacao": 16},
    {
        "titulo":"Rei Leão",
        "classificacao": 12},
    {
        "titulo":"Lagoa Azul",
        "classificacao": 16},
    {
        "titulo":"Ninja Assassino",
        "classificacao": 18},
]

idade = int(input('Qual a sua idade? '))
while idade < 0:
    print('Idade inválida')
    idade = int(input('Qual a sua idade? '))
for filme in filmes:
    if idade >= filme['classificacao']:
        print(f'você pode assistir ao filme {filme["titulo"]}')
    elif idade < filme['classificacao']:
        print(f'o filme {filme["titulo"]} Você ainda não tem idade para este filme')