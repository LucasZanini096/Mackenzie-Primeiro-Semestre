#Jornadas das estrelas 
import math
#Primeira linha 
estrelas = int(input("Digite o número de estrelas:"))

if estrelas <= math.pow(10,6) and estrelas >= 1:
    #Estrela i -> carneiros = 1
    carneiro = 1
    for i in range (1,estrelas+1):
        print (i)
        """while x <= estrelas:
            carneiro = carneiro +2
            lista = []
            lista.append(carneiro)
            print (lista)"""





