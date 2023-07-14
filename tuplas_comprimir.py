lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

tupla_dos = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 0)

# la compresion de listas es una forma de crear listas de forma dinamica
# si una tupla tiene más longitud que otra la diferencia se ignora al momento de comprimir
resultado = zip(tupla, tupla_dos) # -> zip

tupla_resultado = tuple(resultado) 
print(tupla_resultado)
