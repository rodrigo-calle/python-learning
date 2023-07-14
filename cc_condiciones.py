# resultado = 10

# if resultado > 10:
#     print("El resultado es mayor a 10")
# else:
#     print("El resultado es menor o igual a 10")


calificacion = 11

if calificacion >= 18:
    print("Aprobado con una super " + str(calificacion) + " puntos")
elif calificacion >= 13:
    print("Aprobado con " + str(calificacion) + " puntos")
elif calificacion >= 10:
    print("Debes mejorar, pero aprobaste con " + str(calificacion) + " puntos")
else:
    print("Reprobaste con " + str(calificacion) + " puntos")


# Asignando valor a una variable por tipo de valor

mi_variable = 10 or 'Hola mundo' # Asigna el primer valor que no sea False, en este caso 10

print(mi_variable) # 10

mi_variable_dos = 0 or 'Hola mundo' # Asigna el primer valor que no sea False, en este caso 'Hola mundo'
