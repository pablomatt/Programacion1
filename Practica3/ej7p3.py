comandos = []

palabra = raw_input('Ingrese una palabra ')

dic = {}

#cargo los elementos en la lista
while(palabra<>'0000'):
    comandos.append(palabra)
    palabra = raw_input('Ingrese una palabra ')

comandos.sort() #ordena y agrupa los elementos de la lista

#recorro la lista

for i in range(len(comandos)):

    dic[comandos[i]] = comandos.count(comandos[i]) #cuenta la cantidad de veces que aparece el elemento en la lista
    i = i + 1

print('Lista creada: %s' %(comandos))

print('Diccionario creado: %s' %(dic))

def func(q,r,j):
    o = q * r - j 
    return o 

print(func(3,8,9))