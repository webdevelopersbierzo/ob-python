from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def isPar(x):
    if x % 2 == 0:
        return True
    return False


def suma(a, b):
    return a + b


pares = list(filter(isPar, lista))
print(pares)
resultadoSuma = reduce(suma, pares)
print(resultadoSuma)
