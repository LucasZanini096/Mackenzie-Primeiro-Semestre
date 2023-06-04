#Média final de alunos de uma sala de aula 
#01 - Definir a quantidade de alunos numa sala 
qtd_alunos = int(input("Digite a quantidade de alunos de uma sala:"))
#01.1 - Verificação se qtd_alunos > 0
while True:
    if qtd_alunos > 0:
        break
    else: 
        print ("Digite novamente a quantidade de alunos:")
        qtd_alunos = int(input("Digite a quantidade de alunos de uma sala:"))

#02 - Escrever a nota de cada aluno da turma da prova 1
lista_nota1 = []

for i in range (1,qtd_alunos + 1):
    print (f'Aluno {i}')
    nota_1 = int (input('Digite a nota de 0 a 10 do respectivo aluno'))
    print (nota_1)
    lista_nota1.append(nota_1)

print (f'As notas da primeira prova serão {lista_nota1}')

#02.1 - Lista da nota da prova 2
lista_nota2 = []

for i in range (1,qtd_alunos + 1):
    print (f'Aluno {i}')
    nota_2 = int(input("Digite a nota de 0 a 10 do respectivo aluno:"))
    print (nota_2)
    lista_nota2.append(nota_2)

print (f'A notas da segunda prova serão {lista_nota2}')
#03 - Fazer a média de cada aluno 
media = 0

lista_media = []
for n in range (qtd_alunos):
    media = (lista_nota1[n] + lista_nota2[n])/2
    print (f'A média do aluno {n + 1} será {media}')
    lista_media.append (media)
    #04 - Verficar se ele está aprovado
     
    if media >= 7: 
        print (f'O aluno {n + 1} está aprovado.')
    else:
        print (f'O aluno {n + 1} não está aprovado.')
#05 - Média geral da sala 
Media_geral = (sum(lista_media))/qtd_alunos
print (f'A média geral da sala foi {Media_geral}')
