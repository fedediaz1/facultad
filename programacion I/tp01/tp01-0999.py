
"""
-----------------------------------------------------------------------------------------------
Título: TP - 
Fecha: 03-2024
Autor: Federico Diaz (1182205)

Descripción:
Resolver el siguiente problema utilizando funciones: Un productor frutihortícola desea contabilizar sus cajones de
naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada uno puede
transportar hasta media tonelada (500 kilogramos). En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos
cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. Se
solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden
llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto.
Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del
camión no debe ser inferior al 80%; en caso contrario el camión no será despachado por su alto costo.

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

camiones = int(input('ingresar la cantidad de camiones: '))
pesoQuePuedenLlevarLosCamiones = int(input('ingresar el peso total de cada camion: '))
cantidadDeNaranjasCosechadas = int(input('ingresar la cantidad de naranjas cosechadas: '))

pesoDeCadaNaranja = []
pesoPorCaja = []
naranjasParaJugo = []
cantidadDeCajas = 0

while len(pesoDeCadaNaranja) <= cantidadDeNaranjasCosechadas - 1 and cantidadDeNaranjasCosechadas >= 100:

    peso = random.randint(150,300)
    if peso >= 200:
        pesoDeCadaNaranja.append(peso)   
    else:
        naranjasParaJugo.append(peso)         



#en caso de que se tuviesen que separar las cajas que son para jugo: #esto hace que las cajas se llenen solamente de las naranjas que no son para hacer jugo
#naranjasOptimas = len(pesoDeCadaNaranja) - len(naranjasParaJugo)
#cantidadDeCajas = naranjasOptimas//100
#sobrante = naranjasOptimas - cantidadDeCajas * 100

cantidadDeCajas = len(pesoDeCadaNaranja)//100
sobrante = cantidadDeNaranjasCosechadas - cantidadDeCajas * 100
pesoTotal = 0

for i in range((len(pesoDeCadaNaranja) - sobrante)+1):
    pesoTotal += pesoDeCadaNaranja[i]

camionesALlenar = pesoTotal / pesoQuePuedenLlevarLosCamiones
camionesALlenarExacto = pesoTotal // pesoQuePuedenLlevarLosCamiones
camionesSobrantes = (camionesALlenar - camionesALlenarExacto) 
if camionesSobrantes >= 0.8:
    camionesALlenarExacto += 1
    camionesSobrantes -= 0.8


if cantidadDeNaranjasCosechadas < 100:
    print('no se podria llenar ninguna caja')
else:
    #print(pesoTotal)
    print('hay un total de',len(naranjasParaJugo),'naranjas que son para hacer jugo.')
    print('se podrian hacer un total de',cantidadDeCajas,'cajas, con un sobrante de',sobrante,'naranjas')
    print('se podrian llenar un total de',camionesALlenarExacto,'camiones')
    print('un total de',camiones - camionesALlenarExacto,'no serian despachados por su alto coste')
    
        