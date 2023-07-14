numeros = (1,2,3,4,5, 6, 7, 8, 9, 10)
uno, _, tres, cuatro, cinco, *resto_valores = numeros # para no usar el resto de valores *_ se usa el asterisco 
# * -> resto de valores
# _ -> se usa para ignorar valores

print(uno)
# print(dos)
print(tres)
print(cuatro)
print(cinco)

print(resto_valores)


