#Programa que verifica triângulos 
#1 - Declarar segmentos de reta 
import math
a = float(input("Digite um valor para o segmento a:"))
b = float(input("Digite um valor para o segmento b:"))
c = float(input("Digite um valor para o segmento c:"))
#2 - Verficar a existência de um triângulo 
#Se existir (a <= b + c)
if a >= b + c:
    print ("NAO FORMA TRIANGULO")
else: 
    if math.pow (a,2) == math.pow (b,2) + math.pow (c,2):
        print ("TRIANGULO RETANGULO")
    elif math.pow (a,2) > math.pow (b,2) + math.pow (c,2):
        print ("TRIANGULO OBTUSANGULO")
    else:
        print ("TRIANGULO ACUTANCULO")
if a == b == c:
    print ("TRIANGULO EQUILATERO")
elif a!= b == c or a == b != c or a == c != b:
    print ("TRIANGULO ISOCELES")
else:
    print ("TRIANGULO ESCALENO")

    
        