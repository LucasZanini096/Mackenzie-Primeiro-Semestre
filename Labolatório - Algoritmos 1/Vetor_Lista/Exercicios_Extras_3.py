#Exercício 01

def soma(lista):
  soma_nums = sum(lista)
  return soma_nums

def quantidade(lista):
  qtd_nums = len(lista)
  return qtd_nums

def media(func,lista):
  soma = func(lista)
  media = soma/len(lista)
  return media 

def soma_positivos(lista):
  lista_positivos =[
    positive for positive in lista if positive 
    > 0]
  soma_positivos = sum(lista_positivos)
  return soma_positivos

def qtd_negativos(lista):
  lista_negativos = [
    negative for negative in lista 
    if negative < 0
  ]
  qtd_negativos = len(lista_negativos)
  return qtd_negativos

def media_nums_pares(lista):
  sum_pares = 0
  n_pares = 0
  for num in lista:
    if num % 2 == 0:
      sum_pares += num 
      n_pares += 1
  media_pares = sum_pares/n_pares 
  return media_pares

def percentual_numeros_impares(lista):
  lista_impares = []
  for num_impar in lista:
    if num_impar % 2 != 0:
      lista_impares.append(num_impar)
  return (len(lista_impares)/len(lista)) * 100


lista_nums = []
while True:
  num = input("Digite um número inteiro:")
  
  try:
    num = int(num)
    
    if num == 0:
      break
    
    else:
      lista_nums.append(num)
  
  except ValueError:
    continue

print(soma(lista_nums))
print(quantidade(lista_nums))
print(media(soma,lista_nums))
print(soma_positivos(lista_nums))
print(qtd_negativos(lista_nums))
print(media_nums_pares(lista_nums))
print(percentual_numeros_impares(lista_nums))

#Exercício 02

lista_nums_1 = []

for i in range(5):
  num = int(input("Digite um número inteiro:"))
  lista_nums_1.append(num)
print(soma(lista_nums_1))
print(quantidade(lista_nums_1))
print(media(soma,lista_nums_1))
print(soma_positivos(lista_nums_1))
print(qtd_negativos(lista_nums_1))
print(media_nums_pares(lista_nums_1))
print(percentual_numeros_impares(lista_nums_1))