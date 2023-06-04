
lista_veiculos_consumo = [['Vectra', 9], ['Gol', 10], ['Corsa', 11], ['Fit', 12,5]]
"""
def litros(lista):
  consumo_carros = []
  for i in range(len(lista_veiculos_consumo)):
    for consumo in lista_veiculos_consumo[i][1]:
      consumo_carros.append(consumo)
  litros = [ 1000/x for x in consumo_carros]
  return litros


print(litros(lista_veiculos_consumo))
"""