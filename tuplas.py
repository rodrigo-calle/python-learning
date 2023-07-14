# Listas
cursos  = ['Python' ,  'Django' ,  'Flask' ,  'C' ,  'C++' ,  'C#' ,  'Java' ,  'PHP' ]

# Tuplas
# Permite almacenar datos de cualquier tipo, pero son inmutables
niveles = ('Básico' ,  'Intermedio' ,  'Avanzado', 'Alevin', 'Experto' )

# Subtuplas

subtupla = niveles[0:3:2]
print(subtupla)

# Gerando uma tupla de lista

cursos_tupla = tuple(cursos)

# Gerando una lista de tuplas

niveles_lista = list(niveles)


# Imprimiendo los resultados

print(cursos_tupla)
print(niveles_lista)
