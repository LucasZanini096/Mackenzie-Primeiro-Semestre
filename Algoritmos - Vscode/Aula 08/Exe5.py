#Soma do inverso de fatorial 
#01 - Declarar a quantidade do máximo fatorial 

fatorial_max = int(input("Digite o maior fatorial da sequência:"))

#02 - Cálculo do fatorial
#02. 1 - Condicional para se num é igual a 1 ou 0

cont = 1
anterior = 1
soma = 1
if fatorial_max == 1 or fatorial_max == 0:
    print ("O resultado do inverso da soma será: 1")
else:
    while cont < fatorial_max:
        cont += 1
        fatorial = anterior * cont
        anterior = fatorial 
        soma += 1/fatorial 
    
print ("O resulatdo do inverso da soma será:", \
      "{:.2f}".format(soma)
)


