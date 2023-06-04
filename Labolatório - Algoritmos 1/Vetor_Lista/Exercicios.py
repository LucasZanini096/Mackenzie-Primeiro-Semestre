
#Exercício 01

vetor = []

for indice in range(5):
    n = int(input("Digite um valor inteiro:"))
    vetor.append(n)
    
print(vetor)

#Exercício 02

vetor = []
vetor_invertido = []

for indice in range(10):
    n = int(input("Digite um valor inteiro:"))
    vetor.append(n)
    vetor_ivertido = vetor.reverse()
    
print(vetor_invertido)

#Exercício 03

notas = []

for nota in range (4):
    nota = input("Digite o valor de uma nota:")
    try:
        nota_int = int(nota)
    except:
        print("Digite um número inteiro")
        continue
    notas.append(nota)

sum(notas)
media = sum(notas)/len(notas)
print (f'A média das 4 notas será: {media}')


#Exercício 04

vetor = []
palavra = input("Digite uma palavra qualquer:").lower()
for letra in palavra:
    vetor.append(letra)

n_consoantes = 0
n_vogais = 0

for indice in range(len(vetor)):
    
    if vetor[indice] == "a" or vetor[indice] == "e" or \
       vetor[indice] == "i" or vetor[indice] == "o" or\
       vetor[indice] == "u":
        n_vogais += 1
    
    else:
        n_consoantes += 1

print (f' A palavra digitada possui {n_consoantes} consoantes e {n_vogais} vogais')

#Exercício 05
lista_media_alunos = []
def media (n_alunos):

    soma_notas = 0    
    global lista_media_alunos

    for indice in range(int(n_alunos)):
        
        for x in range(1,5):
            nota = int(input(f"Digite o valor da nota [{x}] do aluno [{indice + 1}] :"))
            soma_notas += nota
        media_aluno = (soma_notas / 4)
        
        lista_media_alunos.append(media_aluno)
    
    n_alunos_superior_7 = 0
    
    for media_requisitada in lista_media_alunos:
        n_alunos_superior_7 += 1 if media_requisitada >= 7 else n_alunos_superior_7 == n_alunos_superior_7
        
    print(f'{n_alunos_superior_7} alunos ficaram com média superior ou igual a 7')

media(5)

