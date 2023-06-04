def entrada():
    num = int(input("Digite um valor inteiro e positivo:"))

    if num > 0:
        return num
    print ("Você digitou um número negativo")

entrada()

def calculaMedia(x,y,z):
    media = (x + y + z)/3
    return media 

