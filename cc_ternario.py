calificacion = 2
color = None

if calificacion >= 18:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion, color)

# Ternario
color = 'verde' if calificacion >= 18 else 'rojo'
