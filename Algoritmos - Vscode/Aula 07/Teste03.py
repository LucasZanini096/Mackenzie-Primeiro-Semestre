#Soma de cinco valores inteiros 
nsomas = 0
soma = 0
while nsomas >= 0 and nsomas <= 5:
    num = int(input("Digite um número:"))
    nsomas += 1
    soma = num + soma

print (soma)