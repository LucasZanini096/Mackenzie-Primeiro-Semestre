#Tabuada do 3
#01 - Numero a ser multiplicado 
NUM =  int(input("Digite o número da tabuada:"))
#02 -  Repetição dos termos da tabuada 
multi_atual = 1

while multi_atual <= 10:
    multiplicacao  = multi_atual * NUM
    multi_atual += 1
    print (multiplicacao)


