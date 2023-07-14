nombre = "Rodrigo Cesar"
apellido = "Calle"

nombre_completo = nombre + ' ' + apellido;

nombre_completo_dos = 'jR. %s %s %s ' % (nombre, apellido, 'Ingeniero')

nombre_completo_tres = 'Jr. {} {}.'.format(nombre, apellido)

nombre_completo_cuatro = 'Sr. {p_nombre} {p_apellido}.'.format(p_nombre=nombre, p_apellido=apellido)

# FS String (interpolación de cadenas)

fs_string = f'Md. {nombre} {apellido}'

print(fs_string)
