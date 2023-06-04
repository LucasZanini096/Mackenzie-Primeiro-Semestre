#Exercício 01
"""
import random

def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

n_elementos_lista = int(input("Digite o número de objetos de uma lista:"))
lista_qualquer = []

for num in range (n_elementos_lista):
    num = random.randint(0,9)
    lista_qualquer.append(num)

print(lista_qualquer)
resposta = (maior_menor(lista_qualquer))

print (f'O maior número e o menor número desta lista será, respectivamente {resposta}')

#Exercício 2
lista_nums = []
def criar_lista(funcao,*args):

    global lista_nums
 
    n_elementos_lista = int(input("Digite o número de objetos de uma lista:"))
    
    for num in range (n_elementos_lista):
        num = random.randint(0,9)
        lista_nums.append(num)
    print(lista_nums)
    return funcao(*args), lista_nums

def media(lista):

    soma_elementos = sum(lista)
    media_lista_nums = soma_elementos / len(lista)
    print (f"A média dos números desta lista será {media_lista_nums}")

media_0 = criar_lista(media, lista_nums)
"""
"""
#Exercício 03

import random

lista_nums = []
def criar_lista(funcao,*args):

    global lista_nums
 
    n_elementos_lista = int(input("Digite o número de objetos de uma lista:"))
    
    for num in range (n_elementos_lista):
        num = random.randint(0,9)
        lista_nums.append(num)
    print(lista_nums)
    return funcao(*args), lista_nums

def verdadeiro_ou_falso(lista):
    num_aleatório = random.choice(lista)
    print(num_aleatório)

    if num_aleatório == max(lista):
        return True 
    return False 

resposta_0 = criar_lista(verdadeiro_ou_falso,lista_nums)
print (resposta_0)

"""
"""
#Exercicio Extra 4 
def inversao(*args):
  lista = [*args]
  lista = lista[::-1]
  print(f'{lista}')

inversao(3,5,6,7,8,9)
"""
#Exercicio Extra 5
"""
lista_veiculos_consumo = [['Vectra', 9], ['Gol', 10], ['Corsa', 11], ['Fit', 12,5]]


def litros(lista):
  lista_litros = []
  
  for bloco in lista:
    for carro in bloco: 
      
      modelo, consumo = carro
      litro = 1000/consumo 
      lista_litros.append(litro)
  
  return lista_litros
                
      
def preco(lista):
  preco_final = [y * 3.9 for y in lista]
  return preco_final


print(litros(lista_veiculos_consumo))

print("-=" * 30)
for i in range (len(lista_veiculos_consumo)):
  print (f'{lista_veiculos_consumo[i][0]} --- {lista_preco_final[i]}')
print("-=" * 30)

"""
#Exercício 06 

def intercalar(lista1,lista2):
  
  lista_intercalada = lista1 + lista2
  





""" 
  if len(lista1) < len(lista2):
    for x in range(len(lista1)):
      lista_intercalada[x] = lista1[x]
      

      cont_1 = 1
      cont_2 = 0

      while cont_2 <= len(lista2):
         lista_intercalada.insert(cont_1,lista1[cont_2])
         
         cont_1 += 2
         cont_2 += 1
    
    return lista_intercalada
  
  else:
     for x in lista2:
      lista_intercalada.append(x)
      
      cont_1 = 1
      cont_2 = 0

      while cont_2 <= len(lista1):
        lista_intercalada.insert(cont_1,lista1[cont_2])
        cont_1 += 2
        cont_2 += 1
    
     return lista_intercalada
  

lista_1 = [1,2,3,4,5,6]
lista_2 = [7,8,9,10,11,12,13]
print(intercalar(lista_1,lista_2))

"""      
