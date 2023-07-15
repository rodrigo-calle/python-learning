# Atributos de clase -> son los atributos que pertenecen a la clase
# Atributos de instancia -> son los atributos que pertenecen a la instancia de la clase o tambien llamados atributos de objeto

class Usuario:
    # Atributos de clase
    username = ''
    email = ''

# __dict__ -> es un meta atributo que contiene todos los atributos de la clase, todos los atributos de la instancia y todos los metodos de la clase heredan estos atributos
# se puede ver con Usuario.__dict__
Usuario.username = 'rodrigo-calle'
Usuario.email = 'rodrigo@gmail.com'

# print(Usuario.username, Usuario.email)
usuario_uno = Usuario()

# para agregar atributos de instacias se hace lo siguiente:

usuario_uno.email = 'rodrigo2@gmail.com'

print(usuario_uno.username, usuario_uno.email)
print(usuario_uno.__dict__)

# Metodo para inicializar una clase

class Vehiculo:

    def initilize(self, color, marca):
        # Agregando atributos de instancia
        self.color = color
        self.marca = marca

carro_uno = Vehiculo()
carro_dos = Vehiculo()

carro_uno.initilize('rojo', 'mazda')
carro_dos.initilize('negro', 'Honda')

print(carro_uno.__dict__)
print(carro_dos.__dict__)

# Inicializando con el método __init__

class Animal:
    # Object
    def __init__(self, nombre='', categoria=''):
        self.nombre = nombre
        self.categoria = categoria  

    def comer(self):
        print('Estoy comiendo')

animal_one = Animal('Perro', 'Cat1')
animal_two = Animal('Gato', 'Cat2')
animal_three = Animal()


print(animal_one.__dict__)
print(animal_two.__dict__)
print(animal_three.__dict__)

# Herencia

class Cuadrupedo:
    def rumiar(self):
        print('Estoy rumiando')


class Caballo(Animal, Cuadrupedo):
    pass

primer_caballo = Caballo('Juan', 'Cat3')

primer_caballo.comer()
primer_caballo.rumiar()

# Sobrescritura de métodos

class Vaca(Cuadrupedo, Animal):
    def __init__(self, edad):
        super().__init__(nombre='', categoria='')
        self.edad = edad

    
    def comer(self):
        super().comer()
        print(f'La vaca {self.nombre} de {self.edad} años esta comiendo ')


vaca_uno = Vaca(edad=10)
vaca_uno.comer()

# Métodos de clase
class Circulo: 
    pi = 3.1416

    @classmethod # Decorador para crear atributos de clase
    def area(cls, radio):
        return cls.pi * (radio**2)
    

resultado = Circulo.area(14)
print(resultado)