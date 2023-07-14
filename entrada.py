nombre = input('Ingresa tu nombre completo:')
edad = input('Ingresa tu edad:')
altura = input('Ingresa tu altura:')

usuario = {
    'nombre': nombre,
    'edad': edad
}

# Convertir un string a un entero
anio_actual = 2023
edad = int(edad)
altura = float(altura)
print('Altura de usuario: ' + str(altura))
print(usuario.get('nombre') + ' tiene ' + usuario.get('edad') + ' años' + ' y nació en el año ' + str(anio_actual - edad))

