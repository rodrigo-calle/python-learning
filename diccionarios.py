elementos = {}

elementos['nombre'] = 'Manzana'
elementos[(1,2,3)] = 'Tupla'

elementos['nombre'] = 'Pera'
print(elementos) # {'nombre': 'Pera', (1, 2, 3): 'Tupla'}

# Obtener un valor

primer_elemento = elementos['nombre']
primer_elemento_dos = elementos.get('nombre', 'Mensaje de error')

print(primer_elemento_dos)

# Clave, valor, item

llaves = elementos.keys()
valores = elementos.values()
items = elementos.items()

# Eliminar un elemento

del elementos['nombre'] # Elimina el elemento de clave 'nombre'
elementos.clear() # Elimina todos los elementos del diccionario
elementos.pop() # Elimina el último elemento del diccionario y devuelve su valor 
