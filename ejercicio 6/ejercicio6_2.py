class Alumno:
    def __init__(self, nombre,  nota):
        self.nombre = nombre
        self.nota = nota

    def imprime_atributos(self):
        print(f"Nombre: {self.nombre} Nota {self.nota}")
    def mostrar_mensaje(self):
        if(self.nota > 5):
            print(f"Has aprobado con una nota {self.nota}")
        else:
            print(f"Has suspendido con una nota {self.nota}")


oscar = Alumno("Oscar", 6)
roberto= Alumno("Roberto", 4)

oscar.imprime_atributos()
oscar.mostrar_mensaje()
roberto.imprime_atributos()
roberto.mostrar_mensaje()