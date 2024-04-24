'''Se ingresan n conjuntos de m valores numéricos cada uno. Se pide informar:
1. Para cada uno de los n conjuntos:
    a. El valor promedio.
    b. El máximo valor.
    c. Porcentaje de valores positivos.
2. Para todo el lote de datos:
    a. Valor promedio.
    b. Porcentaje de valores negativos.
    c. Valor mínimo.
'''


n = int(input('ingresar un valor n: '))
m = int(input('ingresar un valor m: '))

cantidad = n*m


numeros = []

while n > 0:
    while cantidad > 0:
        num = int(input('ingresar un numero para la lista'))    
        numeros.append(num)
        cantidad -= 1
    n -= 1
 
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]


promedio = suma/len(numeros)


print(numeros)

print(promedio)