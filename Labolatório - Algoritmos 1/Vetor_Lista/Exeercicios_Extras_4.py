
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


lista_nums = []
while True:
    num = input("Digite um número inteiro positivo:")
    
    try:
      num = int(num)
      
      if num < 0:
        break
      
      else:
        lista_nums.append(num)
    
    except ValueError:
      continue

texto_0 = "Menu de opções"
print(f'{texto_0:^5}')
texto = """1. Soma dos números digitados
2. Quantidade de números digitados
3. Média dos números digitados
4. Maior número digitado
5. Menor número digitado
6. Sair
"""
print(texto)

while True:
  opcao = int(input("Digite uma opção entre as apresentadas:"))
  
  if opcao == 1:
    soma_nums = soma(lista_nums)
    print(f'A soma dos números digitados é {soma}')
  
  elif opcao == 2:
    print('A quantidade de números digitados é', quantidade(lista_nums))
  
  elif opcao == 3:
    print('A média dos números digitados é', media(soma,lista_nums))
  
  elif opcao == 4:
    maior = 0
    
    for indice in range(len(lista_nums)-1):
      
      if lista_nums[indice] > lista_nums[indice+1]:
        maior = lista_nums[indice]

    print("O maior número da lista é", maior)
  
  elif opcao:
    menor = min(lista_nums)
    print("O menor número da lista é", menor)
  
  else:
    break

#Exercício 02


def indices_acidentes(lista_acidentes):
  max_acidentes = max(lista_acidentes)
  min_acidentes = min(lista_acidentes)

  for i in range(len(lista_acidentes)):
    if lista_acidentes[i] == max_acidentes:
      indice_max = i

  for j in range(len(lista_acidentes)):
    if lista_acidentes[i] == min_acidentes:
      indice_min = i
  print(f"""
--------------------------------------------------------------------------
O número máximo de acidentes foi de {max_acidentes} na cidade {indice_max}
--------------------------------------------------------------------------
O número mínimo de acidentes foi de {min_acidentes} na cidade {indice_min}
--------------------------------------------------------------------------
""")

def media_veiculos(lista_veiculos):
  media = sum(lista_veiculos)/len(lista_veiculos)
  print (f"A média de veículos nas cinco cidades será de {media:2f} carros")


def media_acidentes(lista_acidentes, lista_veiculos):
  lista_num_acidentes = [] #das cidades com menos de 2000 veículos 
  for i in range(5):
    if lista_veiculos[i] < 2000:
      lista_num_acidentes.append(lista_acidentes[i])
  media = sum(lista_num_acidentes)/len(lista_num_acidentes)
  print(f" A média de acidentes de trânsito nas cidades com menos \
         de 2.000 veículos de passeio é de {media:2f} acidentes.")
  


Lista_codigo_cidade = []
Lista_numero_veiculos = []
Lista_numero_acidentes = []

for i in range(5):
  codigo_cidade =  input(f"Digite o código da cidade {i}:")
  Lista_codigo_cidade.append(codigo_cidade)
  numero_veiculos = int(input(f"Digite a quantidade de veículos de passeio da cidade {i}:"))
  Lista_numero_veiculos.append(numero_veiculos)
  numero_acidentes = int(input(f"Digite o número de acidentes da cidade {i}:"))
  Lista_numero_acidentes.append(numero_acidentes)

  