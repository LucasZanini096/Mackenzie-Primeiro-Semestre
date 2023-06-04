#Exercício 01 
#Fazer média das notas 
def media_notas(*args):
  notas = list(args)
  soma_notas = sum(notas)
  return soma_notas/len(notas), notas

def caracteristcas_lista(lista): #Características da lista 

  maior_nota = max(lista)
  menor_nota = min(lista)
  #Achar maior nota 
  contador_1 = 0
  
  for nota_1 in lista:
  
    if nota_1 == maior_nota:
      
      indice_maior_nota = contador_1
    
    else:
      
      contador_1 += 1
  #Achar menor nota
  contador_2 = 0
  
  for nota_2 in lista:
    
    if nota_2 == menor_nota:
      
      indice_menor_nota = contador_2
    
    else:
     contador_2 += 1
  #Printar características
  
  titulo_tabela = "Características da Lista"
  print ("-=" * 30)
  print(f'{titulo_tabela:5^}')
  print(f"Posição Menor Nota: {indice_maior_nota}")
  print(f"Posição Menor Nota: {indice_menor_nota}")
  if 10 in lista:
  
    print("Há a nota 10 na lista de notas")
  else:
    
    print("Não há a nota 10 na lista de notas")

  
media, lista_notas = media_notas(4,5,6)
print(media)

caracteristicas_da_lista = caracteristcas_lista(lista_notas)

#Exercício 02
#Inserir as opções 
lista_nomes = []
while True:
  print(""" 
[1] - Cadrastar um amigo (no final da lista)
[2] - Mostrar os nomes da lista
[3] - Cadrastar um amigo (início da lista)
[4] - Remover um nome 
[5] - Substitui um nome 
[6] - Mostra o número total de amigos 
[7] - Colocar os nomes dos amigos em ordem alfabética
[8] - Sair do programa 
""")
  opcao = input("Digite uma opção entre as oito apresentadas:")
  
  if opcao == "1": #opção 1
    
    nome_cadastro_final = input("Digite um nome para ser cadastrado:")
    lista_nomes.append(nome_cadastro_final)
    
  
  elif opcao == "2": #opção 2
    
    for indice,nome in enumerate(lista_nomes):
      print(f'{indice + 1} -- {nome}')
  
  elif opcao == "4": #opção 4
    
    nome_remover = input("Digite um nome para remover:")
    
    if nome_remover in lista_nomes:
      
      for indice, nome in enumerate(lista_nomes):
        
        if nome == nome_remover:
          
          del(lista_nomes[indice])
    else:
      continue
  
  elif opcao == "3":
    
    nome_cadrasto_inicio = input("Digite um nome para ser cadrastrado:")
    lista_nomes.insert(0,nome_cadrasto_inicio)
  
  elif opcao == "5":
    
    nome_que_sera_subs = input("Digite o nome que será substituido:")
    nome_subs = input("Digite o nome para substituir o antigo:")
    
    for indice, nome in enumerate(lista_nomes):
        
      if nome == nome_que_sera_subs:
        lista_nomes[indice] = nome_subs
  
      else:
        continue
  elif opcao == "6":
    
    num_nomes = len(lista_nomes)
    print('O número de nomes na lista é', num_nomes)

  elif opcao == "7":
    lista_nomes.sort()

  else:
    
    break 
    
        
        
    
    
    
  
    
    
