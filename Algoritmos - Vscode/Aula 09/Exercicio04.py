def menu():
    print("1 - Soma de dois números digitados")
    print("2 - Diferença dos dois números digitados")
    print("3 - Produto dos dois números digitados")
    print ("4 - Divisão dos dois números digitados")
    print ("0 - Sair")

    opcao = input("Digite uma opção entre as apresentadas:")

    if opcao == "1":
        return f'opção 1'
    elif opcao == "2":
        return f'opção 2'
    elif opcao == "3":
        return f'opção 3'
    elif opcao == "4":
        return f'opção 4'
    else:
        print("Você saiu do programa")

opcao_escolhida = menu()
print(opcao_escolhida)
   
def soma(n1,n2):
    return n1 + n2

def diferenca(n1,n2):
    return n1 - n2

def produto(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    if n2 != 0:
        return n1/n2
    print("Essa divisão não é possível!!")

    