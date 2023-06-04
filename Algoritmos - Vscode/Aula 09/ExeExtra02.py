#Exercício extra 03

def area_quadrado (lado):
    area = lado ** 2
    return area

while True:
    lado = int(input("Digite o valor do lado de um quadrado:"))
    
    if lado > 0:
        print(area_quadrado(lado))
        break
    else:
        print("Digite novamente o valor do lado do quadrado")
        continue 
