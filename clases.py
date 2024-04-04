###############################################################################################################
###############################################################################################################
###############################################################################################################
############################################clase 20-3#########################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

"""una funcion permite definir un bloque de codigo reutilizable que se puede ejecutar muchas veces dentro del 
programa principal"""

"""contiene codigo independiente y tiene un proposito especifico"""

"""encapsular intrucciones bajo la forma de una funcion hace que los programas sean mas faciles de leer, mas
simples de mantener y se optimiza el codigo ya que:
-se le saca complejidad al cuerpo principal del programa y se traslada la misma a las funciones
-se modulariza el programa evitando que el cuerpo principal del mismo sea muy extenso
-se redacta una sola vez en una funcion el codigo repetitico, y se la llama las veces que sea necesario."""

"""comentar que es lo que hace la funcion"""

#def nombre(param1, param2):
#    """docstring"""
#    instruccion 1 
#    instruccion 2
#    ...
#    return valor

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#def separadorDeTresLineas():
#    """funcion para imprimir 3 lineas separadoras"""
#    print("--------------------------")
#    print("--------------------------")
#    print("--------------------------")
#    return
##
##programa que muestra mensajes separados por lineas
##
#
#separadorDeTresLineas()
#mensaje = "hola amigo"
#print (mensaje)
#separadorDeTresLineas()
#mensaje = "este es un mensaje para vos"
#print(mensaje)
#separadorDeTresLineas()

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

#def funcionSumadora(num1, num2):
#    """funcion para sumar 2 numeros"""
#    valorSumado = num1 + num2
#    return valorSumado
#
##codigo principal (main)
#...
#...
#x = 5
#y = 10
#z = funcionSumadora(x,y)
#print(z)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

##declaracion de funciones
#def multiplicarNumeros (num1, num2, num3=1, num4=1, num5=1, num6=1):
#    """funcion para multiplicar de 2 a 6 numeros"""
#    resultado = num1 * num2 * num3 * num4 * num5 * num6
#    return resultado
#
##codigo principal (main)
#print(multiplicarNumeros(6,5))      #devuelve 30
#print(multiplicarNumeros(6,5,3))      #devuelve 90
#print(multiplicarNumeros(2,2,2,4))      #devuelve 32
#print(multiplicarNumeros(3,4,2,2,2,-1))      #devuelve -96

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

"""se llama ambito (scope) de una variable al bloque de codigo dentro del cual dicha variable "existe"
es decir, la parte del codigo donde se la puede utilizar, tanto leer como modificar

en un programa basico encontramos 2 categorias de ambito:
-ambito global: region del codigo que pertenece al cuerpo principal del programa
-ambito local (uno o mas): region del codigo que pertenece a una funcion
"""

#modulos en python

##importacion de modulos
#import modulo1
#
##codigo principal
#...
#x = modulo1.funcionX()
#
#if modulo1.funcionY() == ...

#-------------------------------------------------------------------------------------------------

#form modulo1 import funcionX(), funcionY()
#
#x = funcionX
#
#y = funcionY



###############################################################################################################
###############################################################################################################
###############################################################################################################
############################################clase 27-3#########################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

"""funciones lambda"""

"""las funciones lambda son un tipo especial de funcion que tienen una declaracion abreviada
se carcateriza por:
    -la funcion no tiene nombre. se dice que una funcion lambda es anonima
    -toda la funcion se escribe en una unica linea de codigo
    -su declaracion tiene una sentencia return implicita, no hace falta incluir un return

lambda parametros: expresion
        """

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

#agregarIVA = lambda p1: p1 * 1.21
#
#precioSinIVA = float(input("ingresar el valor sin iva: "))
#precioConIVA = agregarIVA(precioSinIVA)
#print("previo con IVA incluido:",precioConIVA)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

#calcularRaiz = lambda v1, v2 : v1 ** (1 / v2)
#
#radicando = int(input("ingrese el valor al cual calcularle la raiz: "))
#indice = int(input("ingrese el indice de la raiz: "))
#
#print(calcularRaiz(radicando,indice))

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


###############################################################################################################
###############################################################################################################
###############################################################################################################
############################################listas#############################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################


"""mutabilidad vs inmutabilidad"""

"""decimos que en python un tipo de objeto es mutable si al modificarle su contenido sigue siendo el mismo objeto(es decir mantiene su identidad o id)
si al modificarle su contenido pasa a ser otro objeto pasa a ser otro objeto (cambia su id)

"""

###############################################################################################################
###############################################################################################################
###############################################################################################################
############################################clase 03-04########################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

#resolver con un for elm in lista:


"""
def cargarAlAzar():
    ...

    return

def calcularProducto(_lista):
    ...

    return producto

def removerElemento(_lista, _valorEliminar):
    ...

    return _lista

def esCapicua(_lista):
    ...

    return capicua

listaBase = cargarAlAzar()

resultado = calcularProducto(listaBase[:]) #se hace una copia de la lista base por si acaso la funcion modifica la lista original y asi se mantiene siempre igual

valorEliminar = int(input("ingresar un valor a eliminar: "))

listaReducida = removerElemento(listaBase.copy(),valorEliminar) #esta es otra manera de mantener la lista original, en este caso, la funcion modifica la lista, por ende es casi obligatorio copiar la lista

if esCapicua(listaBase[:]):
    ...
else:
    ...

"""

#manera para eliminar elemento en una lista:

"""
while valorEliminar in lista:
    lista.remove(valorEliminar)
"""


###############################################################################################################
###############################################################################################################
###############################################################################################################
############################################slicing############################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

#lista[inicio:fin:paso]

"""slicing refiere a la porcion de la lista que va desde el elemento ubicado en el indice INICIO hasta el elemento 
ubicado en el indice ANTERIOR A FIN, avanzando de a cada PASO de elementos"""

"""
lista[6,5,5,8]
lista[1:4:1]
"""

"""si se omite el inicio, python toma desde el primer elemento (o sea, asuma 0)
si se omite fin, python toma hasta el ultimo elemento (o sea, asuma len() )
si se omite el paso, python toma de a un elemento (o sea, asume 1)


tanto inicio como fin soportan indices negativos
prtimerTrimestra = meses[:-9]
ultimo trimestre = mes[-3:]

tambien el paso soporta negatico, pero en este caso el comportamiento es inverso ya que el indice de inicio 
tendra que se mayor que el de fin
"""

#precios = [200,99,500,50,15,400]
#
##a los precios mayores a 100, necesito rebajarle 20 pesos
#for idx, precio in enumerate(precios):
#    if precio > 100:
#        precios[idx] = precios[idx] - 20
#print(precios)


###############################################################################################################
###############################################################################################################
###############################################################################################################
######################################listas por comprension###################################################
###############################################################################################################
###############################################################################################################
###############################################################################################################

"""lista por comprendion es un mecanismo que nos permite crear en una unica linea y de manera muy abreviada, 
una nueva lista a partir de una lista existente

nuevaLista = [expresion for iterador in iterable]

para cada elemento del iterable, python calcula la expresion y entrega el resultado como un nuevo elemento de la nueva lista


preciosSinIva = [100,150,50,33,48,93]

preciosConIva = [precio * 1.21 for precio in preciosSinIva]

print(preciosConIva)




lista por comprension tambien admite el agregado de una condicion que funciona como un filtro con esta sintaxis:

nuevaLista = [expresion for iterador in iterable if condicion]

numeros = [13,8,14,-23,11,-44,0,100]

soloNumerosPares = [numero for numero in numeros if numero % 2 == 0]

print(soloNumerosPares)



tambien es posible en el lugar de la expresion incluid una construccion condicional asi:


nuevaLista = [expresion1 if condicion else expresion2 for iterador in iterable]


precios = 200,99,500,50,15,400

precioRebaja = [precio-20 if precio > 100 else precio for precio in precios]


"""


"""una matriz de 2 dimensiones es una arreglo de elementos organizados en filas y columnas (tmb conocido como array)

cada elemento puede ser referenciado por sus coordenadas [fila] [columna]


en python no existe el tipo de datos array sin embargo, utilizando listas anidadas podemos crear matrices
de dos dimensiones(es decir, mediante una lista de listas)


matriz = [[0,0,0,0,0,0],[0,0,0,0,0,0][0,0,0,0,0,0]]

for fila in matriz:
    print(fila)

    

filas, columnas, relleno = 10,30,0
matriz = []

for i in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(relleno)

for fila in matriz: 
    print(fila)



para trabajar con los elementos de una matriz podemos leerlos o asignarles valores

matriz [0][1] = 7

for fila in matriz:print(fila)

altoFil = len(matriz)
anchoCol = len(matriz [0])
print(altoFil, anchoCol)


for fila in matriz:
    for elem in fila:
        print(elem)

for fil in range(len(matriz)):
    for col in range(len(matriz[0]))
    
    """


"""

filas,columnas,relleno = 10,30,0

matriz_1 = []
for f in range(filas):
    matriz_1.append([relleno] * columnas)

for fila in matriz: print(fila)


"""