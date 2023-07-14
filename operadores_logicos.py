# Operadores lógicos
# Los operadores lógicos son utilizados para evaluar expresiones
# condicionales, y devuelven un valor booleano (True o False).

# Operador and
# Devuelve True si ambos operandos son True
# Devuelve False si uno de los operandos es False
# Ejemplo:

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False

# Operador or
# Devuelve True si uno de los operandos es True
# Devuelve False si ambos operandos son False
# Ejemplo:

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

# Operador not
# Devuelve True si el operando es False
# Devuelve False si el operando es True
# Ejemplo:

# print(not True) # False
# print(not False) # True

# Operadores de identidad
# Los operadores de identidad son utilizados para comparar
# si dos objetos son realmente el mismo objeto, con la misma
# ubicación en la memoria.

# Operador is
# Devuelve True si ambos operandos son el mismo objeto
# Devuelve False si ambos operandos no son el mismo objeto
# Ejemplo:

# x = ['Python', 'Django']
# y = ['Python', 'Django']
# z = x
#
# print(x is z) # True

# Operador is not
# Devuelve True si ambos operandos no son el mismo objeto
# Devuelve False si ambos operandos son el mismo objeto
# Ejemplo:

# x = ['Python', 'Django']
# y = ['Python', 'Django']
# z = x
#   
# print(x is not y) # True

# Operadores de membresía

# Los operadores de membresía son utilizados para evaluar
# si un valor o variable se encuentra en una secuencia.

# Operador in
# Devuelve True si un valor o variable se encuentra en una secuencia
# Devuelve False si un valor o variable no se encuentra en una secuencia
# Ejemplo:

# x = ['Python', 'Django']
# y = 'Python'
#
# print(y in x) # True

# Operador not in
# Devuelve True si un valor o variable no se encuentra en una secuencia
# Devuelve False si un valor o variable se encuentra en una secuencia
# Ejemplo:

# x = ['Python', 'Django']
# y = 'Python'
#
# print(y not in x) # False

# Operadores de asignación
# Los operadores de asignación son utilizados para asignar valores
# a las variables.

# Operador =
# Asigna un valor a una variable
# Ejemplo:

# x = 10
# print(x) # 10

# Operador +=
# Suma el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x += 5
# print(x) # 15

# Operador -=
# Resta el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x -= 5
# print(x) # 5

# Operador *=
# Multiplica el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x *= 5
# print(x) # 50

# Operador /=
# Divide el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x /= 5
# print(x) # 2.0

# Operador %=
# Divide el valor de una variable y el valor especificado, y asigna el resto a la variable
# Ejemplo:

# x = 10
# x %= 5

# print(x) # 0

# Operador //=
# Divide el valor de una variable y el valor especificado, y asigna el resultado entero a la variable
# Ejemplo:

# x = 10
# x //= 5
# print(x) # 2

# Operador **=
# Eleva el valor de una variable a la potencia del valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x **= 5
# print(x) # 100000

# Operador &=
# Realiza una operación AND entre el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x &= 5
# print(x) # 0

# Operador |=
# Realiza una operación OR entre el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x |= 5
# print(x) # 15

# Operador ^=
# Realiza una operación XOR entre el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x ^= 5
# print(x) # 15

# Operador >>=
# Realiza una operación de desplazamiento a la derecha entre el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x >>= 5
# print(x) # 0

# Operador <<=
# Realiza una operación de desplazamiento a la izquierda entre el valor de una variable y el valor especificado, y asigna el resultado a la variable
# Ejemplo:

# x = 10
# x <<= 5
# print(x) # 320

