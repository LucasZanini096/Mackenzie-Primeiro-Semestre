#Pesquisa de uma determinada região 
#01 - Quantidade de pessoas entrevistadas 
qtd_pessoas = int(input("Digite a quantidade de pessoas entrevistadas:"))
#02 - Repetição com estrutura 
count = 1
lista_idade = []
lista_genero = []
while count <= qtd_pessoas:

    print (f'Pessoa {count}')
    idade = int(input("Digite a idade da pessoa respectiva:"))
    genero = input("Digite o gênero da pessoa (M ou F):")
    genero.upper()

    #02.1 - Listar idade e genero

    lista_idade.append(idade)
    lista_genero.append(genero)

    #02.2 - Quebra de laço

    if idade == -1:
        break 

#03 - Dizer qual é a maior idade e a menor idade 

Maior_idade = max(lista_idade)
Menor_idade = min(lista_idade)

print (f'A pessoa com maior idade terá', {Maior_idade}, 'anos.')
print (f'A pessoa com menor idade terá', {Menor_idade}, 'anos.')

#04 - Associação entre idade e gênero
x = 0 
for i in range (qtd_pessoas):
    if lista_idade [i] > 18 and lista_idade [i] < 35 and lista_genero [i] == "F":
        x += 1
#05 - Cálculo da porcentagem    
percentual1 = x/qtd_pessoas
print (f"A porcentagem de mulheres com mais de 65 anos será {percentual1}")
#06 - Porcentagem de pessoas com + de 65 anos 
y = 0
for n in range (qtd_pessoas):
    if lista_idade [n] > 65:
        y += 1
percentual2 = y/qtd_pessoas
print(f'A porcentagem de pessoas com mais de 65 anos será {percentual2}')







