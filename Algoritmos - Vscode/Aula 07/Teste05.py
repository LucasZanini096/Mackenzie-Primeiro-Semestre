#Sequência de números (PA)
n = 0
numero = int(input("Digite um número:"))
nsequencia = int(input("Digite a quantidade de termos desta sequência:"))
while n >= 0 and n <=nsequencia:
    numero1 = numero + (numero*n)
    n += 1
    if n == 1:
        print("O menor número será:", '{}'.format(numero1))
    if n == nsequencia:
        print ("O maior número da sequência será:",'{}'.format(numero1))

           
       