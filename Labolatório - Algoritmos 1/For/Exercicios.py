#Exe 1
"""
#01 Declarar sequência

for i in range (1,100,2):
    print (i)
"""
    
#Exe2
""" 
import math 

for i in range(1,21):
    print(math.pow(i,2))
"""    

#Exe3
"""
#01 - Entrada de número

num = int(input("Digite um número:"))
anterior = 1


#02 - Condição se num == 0 ou == 1:

if num == 0 or num == 1:
    print ("O fatorial desse número será 1")
    
#03 - Condição se num > 1:
else:

    for i in range (1,num + 1)
    mutiplicacao = anterior * i
    anterior = multplicacao

print (f'O fatorial do número {num} será {mutiplicacao}')
"""

"""
#Exe 4

#01 - Contagem a partir do segundo termo
# a2 = 3/2

num = ''
soma = 1

for i in range (3, 100, 2):
    for j in range (2, 51):
        num = i/j
        soma += num

print (f'O resultado dessa soma será {soma:.2f}')
"""

#Exe 5
"""
tabela_conversao = "Tabela de conversão Fahrenheit em Celsius"
escalas = "Celsius    Fahrenheit"
print (f'{tabela_conversao: ^5}')
print (f'{escalas: ^5}')


for f in range (50,151):
    c = 5/9 *(f - 32)
    print (f'{c:.2f}      {f}')
    
"""


#Exe 6

"""
#01 - Entrada de um número

num = int(input("Digite um número:"))
anterior = 1


#02 - Condição se num == 0 ou == 1:

if num == 0 or num == 1:
    print ("O fatorial desse número será 1")
    
#03 - Condição se num > 1:
else:

    for i in range (1,num + 1):
        multiplicacao = anterior * i
        anterior = multiplicacao
        print (f' O fatorial de {i} é {multiplicacao}')
    
"""

# Exe 7
"""
#01 - Entrada da quantidade de funcionários

qtd_funcionarios = int(input("Digite a quantidade de funcionários de uma empresa:"))

cont = 0
cont_b = 0
qtd_mulheres = 0

lista_nomes = []
lista_salarios = []
lista_homens = []
lista_salarios_homens = []
#02 - Repetição do cadrastro de cada funcionário

while cont < qtd_funcionarios:

#03 - Entrada do nome do empregado, seu salário e seu gênero
    
    nome = input("Digite seu nome:")
    
    salario = int(input("Digite seu salário atual:"))
    
    genero = input("Digite seu gênero: [M]asculino ou [F]eminino").upper()


    #04 - Condições de específicas da empresa

    if (genero != "M" or genero != "F") and salario < 850:
        print ("Escreva novamente os dados do funcionário")
        continue

    #05 - Cálculo do novo salário 

    if salario >= 3000:
        salario += (salario * 0.045)
        cont += 1

    elif salario >= 2000:
        salario += (salario * 0.065)
        cont += 1
        cont_b += 1
    
    else:
        salario += (salario * 0.085)
        cont += 1
    
    #06 - Quantidade de mulheres e lista de homens com seus salários

    if genero == "F":
        qtd_mulheres += 1
    else:
        lista_homens.append(nome)
        lista_salarios_homens.append(salario)


    #07 - Inserir valores nas listas 

    lista_nomes.append (nome) #Lista nomes
    lista_salarios.append (salario) #Lista salários 


    


#08 Sáida de dados requisitados no enunciado 
# a  
print ("Tabela do sálarios reajustados")
for indice in range (qtd_funcionarios):
    print (f'{lista_nomes[indice]}  -    {lista_salarios[indice]} reais')
# b 
print (f' {cont_b} trabalhadores receberam um reajuste de 6,5%')

#d
percentual_fem = (qtd_mulheres/qtd_funcionarios) * 100
print (f'O percentual de mulheres nesta empresa é de {percentual_fem}%')

#c
soma_homens = sum(lista_salarios_homens)
media_salario_homens = soma_homens/len(lista_homens)
print (f'A média de salário entre os homens desta empresa é de {media_salario_homens} reais.')


"""
        
    

