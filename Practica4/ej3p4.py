lista = [1000,"Hola","Hola",1000]
cadena = "Soy lo mas capo del mundo "

def longitud(cadena):
    total = 0
    for i in cadena:
        total = total + 1
    return total

longitud(cadena)
print('La longitud es %s ' %(longitud(cadena)))
