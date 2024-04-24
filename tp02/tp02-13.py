import random

'''Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, 
se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga.
Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola 
vez en el informe).

b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los 
registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.
'''

numeroDeSocio = int(input('ingresar numero de socio: '))

listaDeSocios = []

while numeroDeSocio != 0:
    if numeroDeSocio < 10000 or numeroDeSocio > 99999:
        numeroDeSocio = int(input('ingresar un numero de socio de 5 digitos: '))
    
    listaDeSocios.append(numeroDeSocio)
    
    numeroDeSocio = int(input('ingresar otro numero de socio: '))
    
    for elm in listaDeSocios:
        if numeroDeSocio == elm:
            listaDeSocios.remove(elm)
    
    if numeroDeSocio == 0:
        break

eliminarSocio = int(input('ingresar un socio que se dio de baja: '))
while eliminarSocio < 10000 or numeroDeSocio > 99999:
    eliminarSocio = int(input('ingresar un socio valido: '))

print(listaDeSocios)

while eliminarSocio in listaDeSocios:
    listaDeSocios.remove(eliminarSocio)
    
print(listaDeSocios)