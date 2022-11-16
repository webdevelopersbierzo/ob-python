import operaciones


def main():
    resultSuma = operaciones.suma(1, 2)
    print("la suma de 1 + 2 es :", resultSuma)
    resultResta = operaciones.resta(1, 2)
    print("la resta de 1  - 2 es :", resultResta)
    resultMultiplicacion = operaciones.multiplicacion(1, 2)
    print("la multiplicacion de 1  * 2 es :", resultMultiplicacion)
    resultDivision = operaciones.division(10, 5)
    print("la division  de 10/5 es :", resultDivision)


if __name__ == '__main__':
    main()
