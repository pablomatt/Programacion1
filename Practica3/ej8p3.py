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


apariciones = []

for i in dic.keys():
        max_dic = -999999
        print(dic[i])
        if(dic[i] > max_dic):
            max_value = dic[i]
            max_key = i
            tupla = (max_key,max_value)
        if(len(apariciones) == 0):
            apariciones.append(tupla)
        else:
            apariciones.insert(0,tupla)

print('Valor maximo %s ' %(max_value))
print('Clave maxima %s ' %(max_key))

print(apariciones)
