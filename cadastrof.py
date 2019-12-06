from math import *
from string import * 
  
lista_aluno=[] 
lnota1=[]
lnota2=[]
lfalta=[] 
ldiario = [laluno,lhr,lnota1,lnota2,lnota3,lfalta] 
  
aluno=0 
nota1=0
nota2=0
falta=0 
salvar_diario=0 
ini=0
 
#A função que ira ser usada 
def menu (): 
    print ('Menu:') 
    print ('   1 - Matricular aluno') 
    print ('   2 - Remover matricula') 
    print ('   3 - Lançar notas') 
    print ('   4 - Lançar faltas') 
    print ('   5 - Listar alunos matriculados') 
    print ('   6 - Ver o Diário')
    print ('   9 - Sair') 
    opcao = input('Digite a opçao desejada: ') 
    return opcao 
  
def adicionar_matricula ():
    aluno = str(input("Digite o nome do aluno:"))
    if aluno in lista_aluno:
        print('Aluno já está Matriculado')
    else:
        lista_aluno.append(aluno)
        print('Aluno Matriculado') 
    pass 
  
def remover_matricula (): 
    aluno=str(input("Digite o nome do aluno:"))
    if aluno in lista_aluno:
        lista_aluno.remove(aluno) 
        print('Aluno Removido')
    else:
        print('Esse Aluno Não Está Matriculado') 
    pass 
  
def lancar_notas ():
    aluno=str(input("Digite o nome do aluno:"))
    if  aluno in lista_aluno:
        nota1=input("Digite a nota 1 do aluno:")
        nota2=input("Digite a nota 2 do aluno:")
        ldiario.append(nota1)
        ldiario.append(nota2)
    else:
        print('Esse Aluno Não Está Matriculado')
    pass 
  
def lancar_faltas ():
    aluno=str(input("Digite o nome do aluno:"))
    if  aluno in lista_aluno:
        falta=float(input("Digite as faltas do aluno(em hora):")) 
        ldiario.append(falta)
    else:
        print('Esse Aluno Não Está Matriculado')
    pass 
  
def listar_alunos (): 
    print('Alunos Matriculados', lista_aluno) 
    pass 
  
def le_diario (): 
    print(ldiario) 
    pass 
  
def salva_diario (): 
    salvar=input("Deseja salvar o diario:")
    if salvar==sim: 
        print("Diario Salvo") 
    else:
        salvar==não 
        print("Diario não Salvo")
    pass 
  
le_diario() 
opcao = menu() 
while opcao != '9': 
    if opcao == '1': 
        adicionar_matricula() 
    elif opcao == '2':  
        remover_matricula() 
    elif opcao == '3':  
        lancar_notas() 
    elif opcao == '4':  
        lancar_faltas() 
    elif opcao == '5':  
        listar_alunos() 
    elif opcao == '6':
        le_diario()
 
  
    opcao = menu() 
  
salva_diario()