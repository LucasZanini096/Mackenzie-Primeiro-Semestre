
# Programa que replica o método Bubble Sort 

# 01 - Definir a quantidade de elementos de uma lista 

n_elementos = int(input("Digite a quantidade de elementos da lista:"))

#02 - Fazer o input dos números da lista
lista_nums = []

for i in range(n_elementos):
  num = int(input(f"Digite o numero da posição {i}:"))
  lista_nums.insert(i,num)

#03 - Definir uma função para o método bubble 


def Metodo_bubble(lista):
  
   for x in range(len(lista)-1):
    
    for indice in range(len(lista)-1):
        
        if lista[indice] > lista[indice + 1]:
           
           lista[indice] ,lista[indice+1] = lista[indice + 1], lista[indice]
    
   print(lista)
        
      
lista_ordenada = Metodo_bubble(lista_nums)

#Exercício 02
while True:
   

   num_casos = int(input())

   if num_casos >= 1 and num_casos <= 1000:
      break
   
   else:
      continue 
   

def Metodo_bubble(lista):
    num_organizado = ''
    
    for x in range(len(lista)-1):
       
       for indice in range(len(lista)-1):
          
          if int(lista[indice]) > int(lista[indice + 1]):
             
             lista[indice] ,lista[indice+1] = lista[indice + 1], lista[indice]
             
    for alg in lista:
       num_organizado += alg

    return num_organizado   
             
    

for caso in range (num_casos):
   
   entrada_num = input()
   if len(entrada_num) != 4:
       entrada_num = entrada_num.zfill(4)

   entrada_num.split()
   lista_algs = list(entrada_num)
   funcao = Metodo_bubble(lista_algs)        
   print(f'{int(entrada_num)}   {funcao}')

        
        
   
