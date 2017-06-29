lista1 = [2,4,6,"Hola","Perro"]

lista2 = [2,4,7,8,"Bueno","Conejo"]

def superposicion(lista1,lista2):
    for i in lista1:
        for x in lista2:
            if(i == x):
                return True
            else:
                return False

superposicion(lista1,lista2)

print(superposicion(lista1,lista2))
