#Ordem crescente de três números 
print ('Bem vindo ao programa')
a = int(input("Digite um número inteiro:"))
b = int(input('Digite outro número interiro:'))
c = int(input('Digite mais um número inteiro:')) 
if a > b:
    if a > c:
        print (a, ">", b, ">", c)
    elif c > a:
        print (c, ">", a, ">", b)
    else: 
        print (a ,">", c, ">", b)
else: #a < b
    if a > c:
        print (b, ">", a, ">", c)
    elif b > c:
        print (c, ">", b, ">", a)
    else: 
        print (b, ">", c, ">", a)
        