palabra = raw_input('Ingrese una palabra ')

def es_palindromo(palabra):
    if (palabra == palabra[::-1]): 
       return True
    else:
        return False

es_palindromo(palabra)

print(es_palindromo(palabra))
