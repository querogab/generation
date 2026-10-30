def somarmultiplosnumeros(numeros: list):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

def multiplicarmultiplosnumeros(numeros: list):
    total = 1
    for numero in numeros:
        total = total * numero
    return total

def ehpar (numero):
    if numero == int(numero) and numero % 2 == 0:
        return True
    else:
        return False

def ehinteiro (numero):
    if numero == int(numero):
        return True
    else:
        return False 

lista = [5, 10, 15]
print(somarmultiplosnumeros(lista))

lista = [5, 10, 15]
print(multiplicarmultiplosnumeros(lista))
