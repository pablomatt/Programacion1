palabra = raw_input('Ingrese una palabra ')

adivina = raw_input('Ingrese un caracter para adivinar ')

largo = len(palabra)

ok = False


vidas = 4

lista = []

def recorrido(palabra):
    letra = 0
    while((letra <= len(palabra):
        if(adivina == palabra[letra]):
            print('Caracter correcto ')
            
            adivina = raw_input('Ingrese un caracter para adivinar ')
            ok = True

    lista.append(adivina)

if(not ok)
    vidas = vidas - 1
    print('Carcter incorrecto. Te quedan %s vidas ' %(vidas))
    print('Caracteres ingresados : %s ' %(lista))


"""
while((vidas > 0) and (ok == False)):
    if (adivina == palabra):
        print('Ganaste! ')
        ok = True
    else:
        vidas = vidas-1
        print('Palabra incorrecta. Te quedan %s vidas ' %(vidas))
    adivina = raw_input('Ingrese una palabra para adivinar ')


if(vidas > 0):
    print('Juego terminado ')
else:
    print('Te quedaste sin vidas ')

"""