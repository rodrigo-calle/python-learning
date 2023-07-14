# El siguiente bucle recorre una lista de usuarios y los imprime uno por uno:
usuarios = ['Rodrigo', 'Juan', 'Pedro', 'Indira', 'Luis']

for usuario in usuarios:
    print(usuario)

# Break and continue

titulo = "Los ojos de mi princesa"

for caracter in titulo:
    if caracter == 'o' or caracter == ' ':
        continue
        #break # rompe el bucle
    print(caracter)
