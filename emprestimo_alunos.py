# print: comando para imprimir em tela um texto
# \n: uma quebra de linha
print('Bem-vindos ao banco Bauru')
print('Para seu cadastro, preencha as seguintes informações\n')

# criação de variável nome
# input: entrada de dados
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = int(input('Qual seu salário:'))

if idade > 16:
    print('Digite 1 para depósito')
    print('Digite 2 para saque')
    print('Digite 3 para empréstimo')

    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        print('Você escolheu a opção depósito')
        valor_deposito = float(input('Digite o valor de depósito: '))
        if valor_deposito > 0:
            saldo = valor_deposito + salario
            print(f'O valor do seu saldo é de R${saldo}')
        else:
            print('valor não pode ser negativo')
    
    elif escolha == 2:
        print('Vc escolheu a opção de saque')
        valor_saque = float(input('Digite um valor de saque:'))
        if valor_saque < 1000 and valor_saque > 0 and valor_saque <= salario:
            saldo_novo = salario - valor_saque
            print(f'O valor do seu saldo é de R${saldo_novo}')
        else:
            print('saque não foi permitido')

    elif escolha == 3:
        print('vc escolheu a opção emprestimo')
        valor_emprestimo = float(input('Qual valor do emprestimo'))
        if (valor_emprestimo > (salario * 10)) :
            print('O emprestimo não permitido')
        else:
            print('O emprestimo foi aceito')
            divida = valor_emprestimo + salario
            print(f'O valor do seu saldo é de R${divida}')
else:
    print('vc não tem idade para ter conta no banco')