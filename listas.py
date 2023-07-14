# Es una estructura que nos permite manejar un conjunto de datos de forma indexada.

# Se puede instanciar de dos formas:
lista = list()
lista = ["Hola", 1, True, 1.5, [1, 2, 3]]

# Cada elemento de la lista tiene una posición

print(lista[0]) # Hola
print(lista[1]) # 1
print(lista[2]) # True

# Tambien se puede acceder a los elementos de forma inversa

print(lista[-1]) # [1, 2, 3]
print(lista[-2]) # 1.5
print(lista[-3]) # True

# Actualizar elementos de una lista

lista[0] = "Esto es el nuevo valor para la posición 0 de la lista"
print(lista)

# Sublistas
#[start:end]
sub_lista = lista[0:3] # la sublista incluye los elementos desde la posición 0 hasta la posición 2
print(sub_lista)
## Generar una sublista con los elementos desde la posición 2 hasta el final
sub_lista = lista[2:]
## Gemerar dos primeros elementos de la lista
sub_lista = lista[:2]
## Generar una sublista con saltos de 2 en 2
sub_lista = lista[::2]

# Modificar Listas

lista_de_paises = ["Perú", "Colombia", "Argentina", "Chile", "Bolivia", "Ecuador"]

# Agregar un elemento al final de la lista
lista_de_paises.append("Paraguay")
lista_de_paises.append("Venezuela")

# Agregar un elemento en una posición específica

lista_de_paises.insert(0, "México")
print(lista_de_paises)

# Extender una lista con otra lista

lista_de_paises_dos = ["Uruguay", "Brasil"]
lista_de_paises.extend(lista_de_paises_dos)

print(lista_de_paises)

# Eliminar elementos de una lista

lista_de_paises.remove("México")
del lista_de_paises[0]
print(lista_de_paises)

# Eliminar todos los elementos de una lista

lista_de_paises.clear()


# Otros métodos de las listas

lista_numerica = [ 7, 8, 3, 1, 2, 4, 5, 6, 9]

# Ordenar" una lista
##ascendente
lista_numerica.sort()
print(lista_numerica)
##descendente
lista_numerica.sort(reverse=True)
print(lista_numerica)

# Obtener el elemento máximo de una lista

max(lista_numerica)

# Obtener el elemento mínimo de una lista

min(lista_numerica)

# Ver si un elemento se encuentra en una lista

print(10 in lista_numerica) # False

# Ver si un elemento no se encuentra en una lista

print(10 not in lista_numerica) # True

# Obtener indice de un elemento

print(lista_numerica.index(5))
