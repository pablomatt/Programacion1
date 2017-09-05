pal = raw_input('Ingrese una palabra: ')

def palindromo(pal):
    if (pal == pal[::-1]): #recorre de atras para adelante
       return 1
    else:
        return 0

palindromo(pal)

if(palindromo(pal)==1):
    print('La palabra %s es un palindromo ' %(pal))
else:
    print('La palabra %s no es un palindromo ' %(pal))
