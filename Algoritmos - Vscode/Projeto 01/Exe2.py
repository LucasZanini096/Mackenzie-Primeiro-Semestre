#Plano Cartesiano 
#01 Declarar o ponto de origem 
x = int(input("Digite uma coordenada de origem x:"))
y = int(input("Digite uma coordenada de origem y:"))
#02 Declarar o tempo de trajetória
tempo_total = int(input("Digite o tempo de trajetória do robo:")) #Supor que o tempo é 1
#03Declarar variáveis
tempo_decorrido = 0
direita = 0
cima = 0
while tempo_decorrido < tempo_total:
    if tempo_decorrido % 3 == 0 and tempo_decorrido != 0:
        direita += 1
        tempo_decorrido += 2
    else: 
        cima += 1
        tempo_decorrido += 1

cima = cima - 1
#print (direita, cima)
#Declarar xf e yf
xf =  2 * direita + x 
yf = y +  cima
print (f"A coordenada final do robo após o tempo decorrido será ({xf}, {yf})")
 


