#Ejercicio FORMA C

def menu():
    print('''========== MENÚ PRINCIPAL ==========
1. Cupos por tipo de plan
2. Búsqueda de planes por rango de precio
3. Actualizar precio de plan
4. Agregar plan
5. Eliminar plan
6. Salir
=====================================''')

def leer_opcion():
    try:
        opcion = int(input('Ingrese una opción (1-6): '))

        if 1<=opcion<=6:
            return opcion
        return -1
    except ValueError:
        return -1

#OP 1
#se solicita tipo de plan
def cupos_tipo(tipo, planes, inscripciones):
    total = 0

    for plan in planes:
        busqueda = planes[plan][1]

        if tipo.lower() == busqueda.lower():
            cantidad = inscripciones[plan][1]
            total += cantidad
    print(f'El total de cupos disponibles es: {total}')
    return total

#OP 2
#se solicita precios min y max, recorre inscripciones y hace lista
def busqueda_precio(p_min, p_max, inscripciones, planes):
    rango = []

    for codigo in inscripciones:

        if p_min > 0 and p_max > 0 and p_min <= p_max:
            if inscripciones[codigo][1] != 0:
                nombre = planes[codigo][0]
                rango.append(f'{nombre}--{codigo}')
                rango.sort()
        else:
            print('No hay planes en ese rango de precios.')
    print(f'{rango}')

#OP 3
def buscar_codigo(codigo, diccionario):
    if codigo in diccionario:
        return True
    return False

def actualizar_precio(codigo, nuevo_precio, inscripciones):
    for clave in inscripciones:
        if buscar_codigo(codigo, inscripciones):
            inscripciones[codigo][0] = nuevo_precio
            return True
        return False

#OP 4
#solicita: codigo, nombre, tipo, duracion, acceso_piscina, incluye;clases, horario, precio, cupos
#se valida con funciones distintas
#se valida que codigo no exista con buscar_codigo()
def validar_codigo(codigo):
    return codigo.strip() != ''
def validar_nombre(nombre):
    return nombre.strip() != ''
def validar_tipo(tipo):
    if tipo in ('mensual', 'trimestral', 'anual'):
        return True
    return False
def validar_duracion(duracion):
    return duracion > 0
def validar_acceso_piscina(acceso_piscina):
    if acceso_piscina == 's':
        return True
    return False
def validar_incluye_clases(incluye_clases):
    if incluye_clases == 's':
        return True
    return False
def validar_horario(horario):
    return horario.strip() != ''
def validar_precio(precio):
    return precio > 0
def validar_cupos(cupos):
    return cupos >= 0

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, inscripciones, planes):
    registro_plan = [codigo.upper(), nombre.title(), tipo.lower(), duracion, acceso_piscina, incluye_clases, horario.lower()]
    registro_inscrip = [precio, cupos]

    if buscar_codigo(codigo, inscripciones):
        return False
    inscripciones[codigo]= registro_plan
    planes[codigo]= registro_inscrip
    return True

#OP 5
#se solicita codigo que se desea eliminar
def eliminar_plan(codigo, planes, inscripciones):
    if buscar_codigo(codigo, inscripciones):
        del planes[codigo]
        del inscripciones[codigo]
        return True
    return False
#falta imprimir si se borró o no

#main
def main():
    planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
    }

    inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
    }

    opcion = 0
    while opcion != 6:
        menu()
        opcion = leer_opcion()

        if opcion == -1:
            print('Debe seleccionar una opción válida')

        elif opcion == 1:
            tipo = input('Ingrese el tipo de plan: ')

            if cupos_tipo(tipo, planes, inscripciones) == 0:
                print('Tipo de plan inválido')
        elif opcion == 2:
            while True:
                try:
                    minimo = int(input('Ingrese precio mínimo: '))
                    maximo = int(input('Ingrese precio máximo: '))

                    if minimo <= 0 and maximo <= 0 and minimo >= maximo:
                        print('No hay planes en ese rango de precios.')
                        continue
                    busqueda_precio(minimo, maximo, inscripciones, planes)
                    break

                except ValueError:
                    print('Debe ingresar valores enteros')
                    continue
        elif opcion == 3:
            seguir = 's'
            while seguir == 's':
                codigo = input('Ingrese código del plan: ').upper()
                try:
                    nuevo_precio = int(input('Ingrese nuevo precio: '))
                except ValueError:
                    print('Ingrese números enteros.')
                    continue

                if buscar_codigo(codigo, inscripciones) == False:
                    print('El código no existe')
                    continue
                else:
                    actualizar_precio(codigo, nuevo_precio, inscripciones)
                    print('Precio actualizado')
                seguir = input('¿Desea actualizar otro precio (s/n)?: ').lower()
        elif opcion == 4:
            while True:
                codigo = input('Ingrese código del plan: ').upper()

                if not validar_codigo(codigo):
                    print('Código inválido')
                    continue
                elif buscar_codigo(codigo, inscripciones):
                    print('El código ya existe')
                    continue
                break

            while True:
                nombre = input('Ingrese nombre del plan: ').lower()
                if not validar_nombre(nombre):
                    print('Nombre inválido')
                    continue
                break

            while True:
                tipo = input('Ingrese tipo (mensual/trimestral/anual): ')
                if not validar_tipo(tipo):
                    print('Tipo de plan inválido')
                    continue
                break

            while True:
                try:
                    duracion = int(input('Ingrese duración (meses): '))
                    if not validar_duracion(duracion):
                        print('Ingrese duración mayor a 0')
                        continue
                except ValueError:
                    print('Ingrese números enteros')
                    continue
                break

            acceso_piscina = input('¿Incluye acceso a piscina? (s/n): ').lower()
            if not validar_acceso_piscina(acceso_piscina):
                acceso_piscina = False
            acceso_piscina = True

            incluye_clases = input('¿Incluye clases grupales? (s/n): ').lower()
            if not validar_incluye_clases(incluye_clases):
                incluye_clases = False
            incluye_clases = True

            while True:
                horario = input('Ingrese horario: ').lower()
                if not validar_horario(horario):
                    print('Horario inválido')
                    continue
                break

            while True:
                try:
                    precio = int(input('Ingrese precio: '))
                    if not validar_precio(precio):
                        print('Precio debe seer mayor a 0')
                        continue
                except ValueError:
                    print('Ingrese números enteros')
                    continue
                break

            while True:
                try:
                    cupos = int(input('Ingrese cupos: '))
                    if not validar_cupos(cupos):
                        print('Cantidad de cupos inválida')
                        continue
                except ValueError:
                    print('Ingrese números enteros')
                    continue
                break

            if agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, inscripciones, planes):
                print('Plan agregado')
                break
            else:
                print('El código ya existe')
                break

        elif opcion == 5:
            codigo = input('Ingrese código a eliminar: ').upper()
            if not eliminar_plan(codigo, planes, inscripciones):
                print('El código no existe')
                continue
            print('Plan eliminado')

        elif opcion == 6:
            print('Programa finalizado.')
            break

        else:
            print('Opción inválida')

main()
