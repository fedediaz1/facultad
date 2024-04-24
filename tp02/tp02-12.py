"""
-----------------------------------------------------------------------------------------------
Título: TP - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:

Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción
indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un
0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en
el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por
urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def pacientes():
    afiliados = []
    turno = []
    urgencia = []

    numeroDeAfiliado = int(input('ingrese su numero de afiliado: '))
    afiliados.append(numeroDeAfiliado)
    while numeroDeAfiliado != -1:

        while numeroDeAfiliado < 1000 or numeroDeAfiliado > 9999:
            numeroDeAfiliado = int(input('ingresar un numero de afiliado de 4 digitos: '))
            
        urg_O_tur = int(input('ingresar si viene por urgencia(0) o por turno(1): '))


        while urg_O_tur != 1 and urg_O_tur != 0:
            urg_O_tur = int(input('ingresar un numero valido para el turno o urgencia (1/0)'))

        if urg_O_tur == 1:
            turno.append(numeroDeAfiliado)
        elif urg_O_tur == 0:
            urgencia.append(numeroDeAfiliado)



        numeroDeAfiliado = int(input('ingrese su numero de afiliado: '))

        if numeroDeAfiliado == -1:
            break
        afiliados.append(numeroDeAfiliado)

    print('los afiliados que vienen con turno son: ')
    for i in range(len(turno)):
        print(turno[i],end=' ')
    
    print()

    print('los afiliados que vienen por urgencia son: ')
    for i in range(len(urgencia)):
        print(urgencia[i],end=' ')
    
    return urgencia, turno

def busqueda(afiliadosUrg, afiliadosTur, buscar):
    for i in range(len(afiliadosTur)):
        for j in range(len(afiliadosUrg)):
            cantidadUrgencia = 0
            cantidadTurno = 0
            if buscar == afiliadosTur[i]:
                cantidadTurno += 1
            elif buscar == afiliadosUrg[j]:
                cantidadUrgencia += 1
    return cantidadTurno, cantidadUrgencia
            



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

afiliadoPorUrgencia, afiliadoPorTurno = pacientes()
print()
buscar = int(input('ingresar un numero de afiliado a buscar: '))
atTur, atUr = busqueda(afiliadoPorUrgencia, afiliadoPorTurno, buscar)

while buscar != -1:
    while buscar < 1000 or buscar > 9999:
        buscar = int(input('ingresar un numero de afiliado de 4 digitos: '))
    if buscar == -1:
        break
    print('El paciente:', buscar, 'fue atendido', atTur, 'veces por turno y', atUr, 'veces por urgencia.')
    buscar = int(input('Ingresar un numero de afiliado a buscar: '))