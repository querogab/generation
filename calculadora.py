numero1 = float(input("Digite o primeiro número:"))
operador = input("Digite o tipo de conta +, -, /, *:")
numero2 = float(input("Digite o segundo número:"))
resultado = None

if operador == "+":
    resultado = numero1 + numero2

elif operador == "-":
    resultado = numero1 - numero2

elif operador == "*":
    resultado = numero1 * numero2

elif operador == "/":
    resultado = numero1 / numero2

print (resultado)