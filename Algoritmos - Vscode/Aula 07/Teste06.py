#Teste de primo
import math
n = int(input("Digite um número:"))
raiz = math.sqrt(n)
raiz_arredondada = math.floor(raiz)
print (raiz_arredondada)
#Para ser primo, o número necessitar ter apenas dois divisores (1 e ele mesmo)

""" Exemplo: num = 11
 
if num > 1:
 
    
    for i in range(2, num):
 
      
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")"""
