#preço de um produto 
print ("(1) = À vista em dinheiro ou cheque/ (2) = À vista com cartão de crédito/ (3) = Em duas vezes/ (4) = Em três vezes")
preco = float(input("Digite o valor de etiqueta do produto:"))
cp = int(input("Digite a condição de pagamento:"))
if cp == 1:
    pf = preco - (preco * 0.1)
    print ("O preço final a vista será de:", pf, "reais.")
elif cp == 2:
    pf = preco - (preco * 0.05)
    print ("O preço final a vista será de:", pf, "reais.")
elif cp == 3:
    pf = preco/2
    print ("O preço final será de", preco, "em duas parcelas de", pf, "reais.")
else:
    pf = preco + (preco * 0.1)
    pf1 = pf/3
    print ("O preço final será de", pf, "em três parcelas de", pf1, "reais.")
 
