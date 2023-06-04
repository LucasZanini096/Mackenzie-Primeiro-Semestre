#Exe2
"""
soma = int()
for num in range (20, 400 + 1, 2):
    soma += num 

print ('A soma dos fatores dessa sequência é', soma)
"""
#Exe3
"""
h = 1
while True:
    n = input("Digite um número inteiro:")

    try:
        n_int = int(n)
        if n_int >= 2:
            break

    except:
        print('Digite novamente um número inteiro')
        continue 

for i in range (2,n_int + 1):
    inverso = 1/i
    h += inverso 

print (h)
"""
#Exe4
"""
anterior = 0
atual = 1
n = int(input("Digite a quantidade de termos da sequência:"))

while True:
    
    try:
        n_int = int(n)
        break

    except:
        print('Digite novamente um número inteiro')
        continue 

if n == 1 or n == 2:
    print (1)
    print (1)

else:
    for i in range (1,n_int + 1):
        soma = atual + anterior 
        anterior = atual 
        atual = soma 
        print (soma)
""" 
#Exe 5

"""
soma = 100 
anterior = 1
list_fatorial = []
list_dividendo = []

for i in range (1,21):
    multiplicacao = anterior * i
    anterior = multiplicacao
    list_fatorial.append(multiplicacao)

for j in range (99,79,-1):
    list_dividendo.append(j)

    for indice in range (20):
        soma += list_dividendo[indice]/list_fatorial[indice]

print (soma)
"""
#Exe 6
"""
n_divisores = 0
while True:
    n = input("Digite um número inteiro:")

    try:
        n_int = int(n)
        break

    except:
        print('Digite novamente um número inteiro')
        continue 

for divisor in range (1,n_int+1):
    if n_int % divisor == 0:
        n_divisores += 1
        print (f'O número {n} é divisível por {divisor}')
        
print (f"O número {n_int} possui {n_divisores} divisores")
"""

#Exe 8

count = 0
soma_pares_positivos = 0
while count < 50:

    num = int(input('Digite um número inteiro:'))

    if num % 2 == 0 and num > 0:
        print (num)
        soma_pares_positivos += num 

print (soma_pares_positivos)


#Extra
"""
while True:
    lista_pares = []
    
    num = input("Digite um número:")

    try:
       num_verificado = int(num)
    
   except:
       print ("Digite um número inteiro")
       continue
    
    if num % 2 == 0:
        for pares in range (0, num_verficado + 1, 2)
        lista_pares.append(pares)
        leitura_pares = len(lista_pares)

    print (f'A quantidade de pares neste no intervalo é {leitura_pares}')

    else:
        for pares in range (0, num_verficado, 2)
        lista_pares.append(pares)
        leitura_pares = len(lista_pares)

    print (f'A quantidade de pares neste no intervalo é {leitura_pares}')

"""









    




