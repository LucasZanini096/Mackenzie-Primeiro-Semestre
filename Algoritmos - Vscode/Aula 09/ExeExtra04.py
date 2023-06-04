#Exercício extra 05

def Soma_Digitos (num):
  
    num_str = str(num)
    soma = 0
 
    for indice, digito in enumerate(num_str):
        digito = num_str[indice]
        digito_int = int(digito)
        soma += digito_int 
        
    return soma 
    
Soma_Digitos(23)
print(Soma_Digitos(23))




