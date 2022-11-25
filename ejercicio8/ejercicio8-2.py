import pickle


class Vehiculo:
    marca = ""
    modelo = ""
    cilindrada= ""
    precio = 0.0

    def __init__(self,  marca, modelo, cilindrada, precio):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.precio = precio

    def getVehiculo(self):
        return self.marca + " " + self.modelo

Vehiculo1 = Vehiculo("Citroen", "C4" , "1600 cc", 15000)
print(Vehiculo1.getVehiculo())

f = open('datos.bin', 'wb')
pickle.dump(Vehiculo1, f)
f.close()

f = open('datos.bin', 'rb')
datos = pickle.load(f)
f.close();

print(datos.getVehiculo(), 'cilindrada', datos.cilindrada)