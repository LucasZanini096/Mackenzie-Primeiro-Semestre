#Triângulo 
#01 - Declarar o valor da base e da altura 
# Base = Altura 
lado = int(input("Digite o valor da base de um triângulo:"))
#02 - Repetição de *
SIMBOLO = "*"
for i in range (lado + 1):
    altura = i * SIMBOLO
    print (altura)
