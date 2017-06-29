lista = [1,2,3,4,5,6]

def sum(lista):
    suma = 0
    for i in lista:
        print i
        suma = suma + lista[i]
    return suma

def multip(lista):
    mult = 0
    for i in lista:
        mult = mult * lista[i]
    return mult

sum(lista)

multip(lista)

print('La suma de los numeros de la lista es igual a %s ' %(sum(lista)))

print('El resultado de multiplicar los numeros de la lista es igual a %s ' %(multip(lista)))