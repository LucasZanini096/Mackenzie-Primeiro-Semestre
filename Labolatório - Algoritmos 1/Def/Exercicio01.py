#Soma de três números 
def soma_tres_numeros(n1,n2,n3):
    print (f'{n1} + {n2} + {n3} = {n1+n2+n3}')

soma_tres_numeros(2,3,5)

def verficacao_num (num):
    if num == 0 or num < 0:
        return "N"
    return "P"


