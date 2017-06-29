palabra = raw_input('Ingrese una palabra ')

def es_palindromo(palabra):
    if (palabra == palabra[::-1]): 
       return True
    else:
        return False

es_palindromo(palabra)

if(es_palindromo(palabra) == True):
    print('La palabra %s es un palindromo ' %(palabra))
else:
    print('La palabra %s no es un palindromo ' %(palabra))