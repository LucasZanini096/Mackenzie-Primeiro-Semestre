# Dia aletório na semana 
# 1 - tabela 
print ('Bem vindo ao programa')
print ('Valor - Dia da Semana')
print ('0 - Segunda-Feira')
print ('1 - Terça-Feira')
print ('2 - Quarta-Feira')
print ('3 - Quinta Feira')
print ('4 - Sexta-Feira')
print ('5 - Sábado')
print ('6 - Domingo')
#02 - Declarar variáveis 
dia = int(input("Digite o dia:"))
mes = int(input("Digite o número referente a um mês:"))
ano = int(input("Digite um ano:"))
#03 Formula 
DiaSemana = ((ano - 1901) * 365 + (ano - 1901)) / (4 + dia + (mes - 1) * 31 - ((mes * 4 + 23) / 10) * ((mes + 12) / 15) + ((4 - ano % 4)) * ((mes + 12)/15))
print (DiaSemana)