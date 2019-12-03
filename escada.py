# Faça uma escadinha:

for i in range(6):
    print(str(i) * i) 

# ano

dia = int(input('Dia do seu nascimento:'))
mes = int(input('Mês do nascimento:'))
ano = int(input('ano do nascimento:'))

diasDeVida = ((2019-ano)*360)+(mes*30)+dia

print('Você já viveu {} dias.'.format(diasDeVida))