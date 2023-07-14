# String
titulo_curso = 'Curso Profesional de Python'
### String con salto de línea
titulo_curso_salto_de_linea = '''Curso Profesional de Python
con Django Framework'''
# Integer
numero_estudiantes = 100 #-2, -1, 0, 1
# Float
precio = 99.99
# Boolean
disponible = True
# List
estudiantes = ['Rodrigo', 'Juan', 'Pedro']
# Tuple
clases = ('Clase 1', 'Clase 2', 'Clase 3')
# Dictionary
estudiante = {
    'nombre': 'Rodrigo',
    'edad': 25,
    'cursos': ['Python', 'Django', 'JavaScript']
}
# None
nulo = None
# Type
print(type(titulo_curso))
print(type(titulo_curso_salto_de_linea))
print(type(numero_estudiantes))
print(type(precio))
print(type(disponible))
print(type(estudiantes))
print(type(clases))
print(type(estudiante))
print(type(nulo))

# Operadores aritméticos
# Suma
print(1 + 1)
# Resta
print(2 - 1)
# Multiplicación
print(2 * 2)
# División
print(4 / 2)
# División entera
print(4 // 2)
# Módulo
print(4 % 2)
# Exponente
print(2 ** 2)
 

# Tipado Dinámico
# Python es un lenguaje de tipado dinámico, es decir, 
# no es necesario declarar el tipo de dato de una variable,
# Python lo infiere automáticamente.
# Ejemplo:

valor = 10
valor = 'Rodrigo'
valor = True
print(valor)
