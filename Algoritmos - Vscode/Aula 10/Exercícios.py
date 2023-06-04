import random
"""
#Exercício 03
def cadrastar_produto(lista):
    produto = {}
    
    nome = input("Digite o nome do produto:")
    qtd = int(input("Digite a quantidade desse produto:"))
    valor = int(input("Digite o valor unitário desse produto:"))
    
    produto.update(
       
        Produto=nome, 
        Quantidade=qtd,
        Valor_reais=valor      
    )
    lista.append(produto)
    return lista

def remove_product(lista):
    produto_removido = input("Digite um nome do produto para ser removido:")
    contador = 0
    for produto in lista:
        if produto_removido in produto.values():
            del lista[contador]
            return lista
        else:
            contador += 1

def soma_valores(lista):
    soma_total = 0
    for produto in lista:
        soma_total += produto["Quantidade"] * produto["Valor_reais"]
        print (f'A soma total dos produtos será {soma_total} reais')

def exibir_produtos(lista):
    for produto in lista:
        print(produto)

#Print Tabela 

lista_produtos =[]
while True:
    titulo = "++++++++++Armazém da Vila++++++++++"
    print(f'{titulo: ^10}')
    print()
    print("""
   # 1. Cadastrar produto
   # 2. Remover produto
   # 3. Calcular valor do estoque
   # 4. Exibir produtos
   # 5. Sair

""")
    print("+" * 35)
    print()
    opcao = input("Digite sua opção:")

    if opcao == "1":
        cadrastar_produto(lista_produtos)
    elif opcao == "2":
        remove_product(lista_produtos)
    elif opcao == "3":
        soma_valores(lista_produtos)
    elif opcao == "4":
        exibir_produtos(lista_produtos)
    else:
        break 
"""
"""
#Exercício 04

def exibir_notas(lista):
    print("++++++Tabela de Notas++++++")
    print()
    for i in range(len(lista)):
        print(f'Nota aluno [{i}] - {lista[i]}')

def exibir_notas_ordem_inversa(lista):
    lista_inversa = lista.reverse()
    for i in range(len(lista)):
        print(f'Nota aluno [{i}] - {lista[i]}')    

def soma(lista):
  soma_nums = sum(lista)
  return soma_nums

def media(func,lista):
  soma = func(lista)
  media = soma/len(lista)
  return media 

def notas_acima_da_media(media,lista):
    n_notas_acima = 0
    for nota in lista:
        if nota > media:
            n_notas_acima += 1
    print(f"O número de notas acima da média é {n_notas_acima}")

lista_notas = []
while True:
    num = input("Digite um número inteiro positivo:")
    
    try:
      num = int(num)
      
      if num < 0:
        break
      
      else:
        lista_notas.append(num)
    
    except ValueError:
      continue

exibir_notas(lista_notas)
print()
exibir_notas_ordem_inversa(lista_notas)
print()
soma(lista_notas)
print()
media_nums = media(soma,lista_notas)
print(f"A média da soma das notas é {media_nums:.2f}")
print()
notas_acima_da_media(media_nums,lista_notas)
"""
#Exercício 05
"""
def lista_str(str):
   lista = []
   for i in range(len(str)):
      lista.append(str[i])
   print(lista)
   
palavra = input("Digite uma palavra:")
lista_str(palavra)

#Exercício 06 e 07 

def lista_frase_str(frase):
   frase_separada = frase.split(" ") #O que coloca dentro do split é o que vai distinguir os objetos de uma lista
   print(frase_separada)

frase = "Eu sou muito legal"
lista_frase_str(frase)
"""
#Exercício 08

def nome_alg_de_um_num(num):
   lista_algs = [0,1,2,3,4,5,6,7,8,9]
   lista_nomes_algs = [
      "zero","um","dois","três",
      "quatro","cinco","seis","sete",
      "oito","nove"
   ]
   lista = []
   lista_nomes = []
   for i in range(len(num)):
      lista.append(num[i])


   for numero_1 in lista:
      contador = 0
      for numero_2 in lista_algs:
          if numero_1 == str(numero_2):
              lista_nomes.append(lista_nomes_algs[contador])
          else:
             contador += 1
   print(tuple(lista_nomes))

numero = "1234"
nome_alg_de_um_num(numero)      

#Exercício 09

lista = []
for i in range(20):
   num_aleatório = random.randint(0,100)
   lista.append(num_aleatório)

print(lista)
print(f'O maior número da lista é {max(lista)}.')
print(f'O menor número da lista {min(lista)}.')



   











