#Cálculo de imposto

preco_final = 0
def somaImposto(taxaImposto, custo):
    global preco_final
    preco_final = ((taxaImposto/100) * custo) + custo 
    return print(f' O preço final de custo será {preco_final} reais')

somaImposto(24,36) 



