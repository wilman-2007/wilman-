class Perro:
    def __init__(self, edad, nombre, color):
        self.edad = edad
        self.nombre = nombre
        self.color = color

    def comer(self):
        print(f"Mi perro {self.nombre} está comiendo.")

    def jugar(self):
        print(f"Mi perro {self.nombre} está jugando.")

    def acariciar(self):
        print(f"Estoy acariciando a mi perro {self.nombre}.")

# Crear un objeto de la clase Perro
mi_perro = Perro(2, "Firulais", "negro")

# Imprimir los atributos del objeto
print(f"Mi perro se llama {mi_perro.nombre}, tiene {mi_perro.edad} años y es de color {mi_perro.color}.")

# Llamar a los métodos del objeto
mi_perro.comer()
mi_perro.jugar()
mi_perro.acariciar()
