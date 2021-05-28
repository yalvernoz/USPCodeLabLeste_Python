num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))

print("1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão, 5 - Divisão Inteira, 6 - Resto da Divisão, 7 - Potencia")
operacao = int(input("Digite o codigo da Operacao:"))

if operacao < 1 or operacao > 7:
    print("Operacao Invalida!")
else:
    print("Número 1:", num1)
    print("Número 2:", num2)
    if operacao == 1:
        print("Soma:", num1+num2)
    elif operacao == 2:
        print("Subtração", num1-num2)
    elif operacao == 3:
        print("Multiplicação", num1*num2)
    elif operacao == 4:
        print("Divisão", num1/num2)
    elif operacao == 5:
        print("Divisão Inteira:", num1//num2)
    elif operacao == 6:
        print("Resto da Divisão:", num1%num2)
    elif operacao == 7:
        print("Potência", num1**num2)