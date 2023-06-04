contNum = 1
while contNum <= 3:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número", num, "é par.")
        contNum = contNum + 1
    else:
        print("O número", num, "é ímpar.")
        contNum = contNum + 1
