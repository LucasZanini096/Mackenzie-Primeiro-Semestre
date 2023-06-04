def grafBar(*args):
    simbolo = "*"
    for num in range(len(args)):
        saida = simbolo * int(args[num])
        print (saida)
        
    
grafBar(1,2,3,4,5,6)

numeros = 1,2,3,4,5,6 #Isso aqui é uma tupla 
print(grafBar(numeros)) #Vai dar erro !!

#Solução 

numeros = 1,2,3,4,5,6
print(grafBar(*numeros))


