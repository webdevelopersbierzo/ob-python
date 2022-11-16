class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):

        self.velocidad = velocidad
        self.cilindrada = cilindrada
        super().__init__(color,ruedas,puertas)

coche1 = Coche('rojo', 4, 5, 200, 1600)

print(f"El objeto creado es un coche llamado coche1 con color {coche1.color} con {coche1.ruedas} ruedas")
print(f"y {coche1.puertas} puertas con una velocidad de {coche1.velocidad} y una ciclindrada de {coche1.cilindrada}")



