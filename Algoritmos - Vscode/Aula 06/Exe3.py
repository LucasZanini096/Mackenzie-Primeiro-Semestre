import math
print ("Seja bem vindo ao programa")
lado = float(input("Digite o valor do lado do cubo em metros:"))
consumo_medio = float(input("Digite o valor do consumo médio em litros por dia:"))
volume = math.pow (lado,3)
volume1 = volume * 1000
print ("O volume do reservatório em centimetros cúbicos será:", volume1)
autonomia = volume/consumo_medio
autonomia1 = volume // consumo_medio 
r =  autonomia - autonomia1
horas = r * 24 
print ("A autonomia do reservatório será de", autonomia1 , "dias e", horas, "horas.")
if autonomia < 2: 
    print ("O consumo está elevado")
elif (autonomia > 2) and (autonomia < 7):
    print ("O consumo está moderado")
else:
    print ("O consumo está reduzido")