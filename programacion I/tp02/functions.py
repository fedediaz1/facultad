import random
def devolverNombreDelMes(numDelMes):
    mes = ''
    if numDelMes == 1:
        mes = 'enero'
    elif numDelMes == 2:
        mes = 'febreo'
    elif numDelMes == 3:
        mes = 'marzo'
    elif numDelMes == 4:
        mes = 'abril'
    elif numDelMes == 5:
        mes = 'mayo'
    elif numDelMes == 6:
        mes = 'junio'
    elif numDelMes == 7:
        mes = 'julio'
    elif numDelMes == 8:
        mes = 'agosto'
    elif numDelMes == 9:
        mes = 'septiembre'
    elif numDelMes == 10:
        mes = 'octubre'
    elif numDelMes == 11:
        mes = 'noviembre'
    else:
        mes = 'diciembre'
    return mes
    
def cargarListaConNumerosAlAzar():
    lista = []
    cantidadDeNumeros = random.randint(10,99)
    for _ in range(cantidadDeNumeros):
        lista.append(random.randint(1000,9999))
    return lista

def productoDeElementosEnListas(lista):
    total = 0
    for i in range(len(lista)):
        total *= lista[i]
    return total

def esCapicua(lista):
    lista2 = lista[::-1]
    if lista2 == lista:
        return True

def numerosImpares():
    numeros_impares = [x for x in range(100, 201) if x % 2 != 0]
    print(numeros_impares)

def es_impar(numero):
    return numero % 2 != 0


