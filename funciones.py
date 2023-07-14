def suma_total(numero_uno, numero_dos):
    return numero_uno + numero_dos

# numero_uno = int(input("Ingrese el primer numero: "))
# numero_dos = int(input("Ingrese el segundo numero: "))

print(suma_total(4, 89))

# Funciones de parámetros opcionales

def area_circulo(radio, pi=3.1416):
    return pi * (radio**2)


print(area_circulo(4))

# Tambien se puede colocar el nombre del parametro al usar la funcion, al hacer esto no importa el orden de los parametros

print(area_circulo(pi=3.14, radio=4))

# Funciones con un numero indeterminado de argumentos

def promedio(*args): # El asterisco indica que se recibira un numero indeterminado de argumentos, se llama args
    print(type(args))
    return sum(args) / len(args)

print('El resultado es '  + str(promedio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

def combinacion(p1,p2,*args, p4):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(1, 2, 3,1,'hola', 'mundo', p4=4)

# para que los args dejen de ser tuplas y pasen a ser listas se debe hacer lo siguiente

def promedio_dos(**kwargs):
    print(kwargs)
    print(type(kwargs))

promedio_dos(rodrigo=[20, 18, 14], jose=[15, 6, 20]) # importante es no dejar espacios

# funciones combinadas

def combinacion_dos(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion_dos(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, rodrigo=[20, 18, 14], jose=[15, 6, 20])

# Scope

animal = 'Leon' # Variable global

def imprimir_animal():
    animal = "Ballena"
    print(animal)

imprimir_animal()
print(animal) # podemos visualizar la diferencia de variable llamando los ids de cada una. Eso se puede hacer con id()

# Funciones Anidadas

def operacion(cantidad, total, tipo='deposito'):


    def deposito(cantidad, total):
        return cantidad + total


    def retiro(cantidad, total):
        if(total >= cantidad):
            return total - cantidad
        else:
            return None

    if(tipo == 'deposito'):
        return deposito(cantidad, total)
    elif(tipo == 'retiro'):
        return retiro(cantidad, total)

resultado = operacion(10, 303)
print(resultado)

# Ciudadanos de primera clase

# Las funciones son ciudadanos de primera clase, esto quiere decir que se pueden asignar a variables
# y se pueden pasar como argumentos a otras funciones y pueden retornar otras funciones

def centigrados_a_farenheit(grados):
    return grados * 1.8 + 32

mi_funcion = centigrados_a_farenheit

print(mi_funcion(32))
print(mi_funcion(-5))
print(mi_funcion(100))

# Funciones Lambda

# Son funciones anonimas, es decir, no tienen nombre

funcion_grados = lambda grados : grados * 1.8 + 32 # lambda <argumentos> : expresion

print(funcion_grados(32))


"""
 Funcion lambda sin parametros

 parametros_default = lambda : p1=10, p2=20, p3=30 : p1 + p2 + p3

 asterisco = lambda *args : **kwargs : len(args) + len(kwargs)
"""

# callbacks

# Son funciones que se pasan como argumentos de otras

promedio = lambda *args : sum(args) / len(args)
aprobatorio = lambda calificacion : calificacion >= 13

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'El promedio {promedio} es aprobatorio')
    else:
        print('No aprobaste la materia')

mostrar_mensaje(promedio, aprobatorio, 10, 20, 13, 14, 11)

# Variables no locales

# Es una funcion que regresa otra funcion
e = 'e'
def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'
        nonlocal b # hace que se tome la variable b de la funcion principal
        b = 'Cambio de valor de b'

        print(a, b, c, e), 
    funcion_anidada()
    print(b)

funcion_principal()


# Retornar funciones
## Esto es una característica que pertenece a ciudadano de primera clase
def saludar():

    def mostrar_mensaje():
        print('Hola Mundo')

    return mostrar_mensaje

respuesta = saludar()
respuesta()

# Clousure

