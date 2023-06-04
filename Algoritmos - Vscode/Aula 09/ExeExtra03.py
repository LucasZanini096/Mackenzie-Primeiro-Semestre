#Exercício extra 04

def fatorial(num):
    anterior = 1

    if num == 0 or num == 1:
        return 1
    
    else:
        
        for i in range(1,num+1):
            multiplicacao = i * anterior
            anterior = multiplicacao 
        return multiplicacao
        
        
n_fatoriais = int(input("Digite o número de fatoriais desejado:"))

print (f"TABELA DE FATORIAIS (0 A {n_fatoriais} )")

lista_fatoriais = [fatorial(num) for num in range(0,n_fatoriais + 1)]

print ("-=" * 30)

for indice, numero in enumerate(lista_fatoriais):
    print(f'{indice}  ---  {numero}')

print ("-=" * 30)



