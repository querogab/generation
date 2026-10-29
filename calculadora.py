numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
operador = input("Digite o tipo de conta +, -, /, *:")

if operador == "+":
    print(numero1 + numero2)

elif operador == "-":
    print(numero1 - numero2)

elif operador == "*":
    print(numero1 - numero2)

elif operador == "/":
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else: 
        print(numero1 / numero2)

else:
    print("Operador inválido")