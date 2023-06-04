def exibeMsg():
    print ("Escreva um programa modularizado \
que permite ao usuário converter uma faixa de temperatura de Fahrenheit para Celsius (O\
usuário deve digitar F) e de Celsius para Fahrenheit (O usuário deve digitar C)")

def getConvertTo(texto):
    if texto == "F":
        return "F"
    return "C"

def exibeFahrenheitTOCelsius(start,end):
    C = (5 * (end-start-32)) / 9
    print (f'A variação da temperatura em Fahrenheit\
            convertida em Celsius terá como resultado: {C}')

def exibeCelsiusTOFahrenheit(start,end):
    F = (9 * (end-start + 32))/ 5
    print (f'A variação da temperatura em Celsius\
            convertida em Fahrenheit terá como resultado: {F}')

























