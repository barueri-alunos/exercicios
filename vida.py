def calcular_vida(ano_atual, ano_nasceu, mes):
    idade = ano_atual - ano_nasceu
    meses = mes * 30
    dias_vida = (idade * 365) + meses
    
    print(dias_vida)


print("Quantos anos vc viveu?")

ano1 = int(input("Digite o ano atual: "))
ano2 = int(input("Digite o ano que nasceu: "))
mes = int(input('Mês do nascimento:'))

calcular_vida(ano1, ano2, mes)