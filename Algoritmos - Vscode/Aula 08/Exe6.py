import math
#01 - Declarar um valor X
x = input("Digite um valor inteiro:")
#01.1 - Verficar se o usuário digitou um número inteiro 
try:
    print(x)
    x_int = int(x)
except:
    print ("Você não digitou um número inteiro")

#02 - Escrever a expressão (Parte1)

pares = []
impares = []
if x_int % 2 == 0:

    for i in range (2,x_int + 1, 2): #Números elevados a um expoente par
       
        par = math.pow(x_int,i)
        pares.append(par)

        for j in range (1,x_int,2): #Números eleavdos a um exponte ímpar

            impar = math.pow(x_int,j)
            impares.append(impar) 
else:
    for i in range (2,x_int, 2): #Números elevados a um expoente par
       
        par = math.pow(x_int,i)
        pares.append(par)

        for j in range (1,x_int + 1,2): #Números elevados a um expoente ímpar 

            impar = math.pow(x_int,j)
            impares.append(impar) 

#03 - Escrever a expressão (Parte2)
#03.1 -Inverter a ordem das listas 

pares.reverse()
impares.reverse()

 








