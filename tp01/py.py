import random


#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def naranjas():
    listaDeNaranjas = []
    naranjasParaJugo = []
    cantidadDeNaranjasCosechadas = int(input('ingresar la cantidad de naranjas cosechadas: '))

    while len(listaDeNaranjas) <= cantidadDeNaranjasCosechadas - 1 and cantidadDeNaranjasCosechadas >= 100:

        peso = random.randint(150,300)
        if peso >= 200:
            listaDeNaranjas.append(peso)   
        else:
            naranjasParaJugo.append(peso)
        
    return cantidadDeNaranjasCosechadas, listaDeNaranjas, naranjasParaJugo

def calcularElPesoTotalYElSobrante():
    #en caso de que se tuviesen que separar las cajas que son para jugo: #esto hace que las cajas se llenen solamente de las naranjas que no son para hacer jugo
    #naranjasOptimas = len(listaDeNaranjas) - len(naranjasParaJugo)
    #cantidadDeCajas = naranjasOptimas//100
    #sobrante = naranjasOptimas - cantidadDeCajas * 100
    
    cantidadDeCajas = len(listaDeNaranjas)//100

    sobrante = cantidadDeNaranjasCosechadas - cantidadDeCajas * 100

    pesoTotal = 0
    for i in range((len(listaDeNaranjas) - sobrante)+1):
        pesoTotal += listaDeNaranjas[i]
    return pesoTotal, sobrante, cantidadDeCajas



def calcularElSobranteParaLosCamiones():
    camionesALlenar = pesoTotal / pesoQuePuedenLlevarLosCamiones

    camionesALlenarExacto = pesoTotal // pesoQuePuedenLlevarLosCamiones

    camionesSobrantes = (camionesALlenar - camionesALlenarExacto) 

    if camionesSobrantes >= 0.8:
        camionesALlenarExacto += 1
        camionesSobrantes -= 0.8

    return camionesALlenarExacto

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

camiones = int(input('ingresar la cantidad de camiones: '))
pesoQuePuedenLlevarLosCamiones = int(input('ingresar el peso total de cada camion: '))

pesoPorCaja = []
      
cantidadDeNaranjasCosechadas, listaDeNaranjas, naranjasParaJugo = naranjas()
pesoTotal, sobrante, cantidadDeCajas = calcularElPesoTotalYElSobrante()
camionesALlenarExacto = calcularElSobranteParaLosCamiones()


if cantidadDeNaranjasCosechadas < 100:
    print('no se podria llenar ninguna caja')
else:
    #print(pesoTotal)
    print('hay un total de',len(naranjasParaJugo),'naranjas que son para hacer jugo.')
    print('se podrian hacer un total de',cantidadDeCajas,'cajas, con un sobrante de',sobrante,'naranjas')
    print('se podrian llenar un total de',camionesALlenarExacto,'camiones')
    print('un total de',camiones - camionesALlenarExacto,'no serian despachados por su alto coste')
    
        