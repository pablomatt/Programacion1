
nom = raw_input('Ingrese un nombre ')

ape = raw_input('Ingrese un apellido ')

edad = input('Ingrese una edad ')

dni = input ('Ingrese un dni ')

clave = dni*(len(nom)+len(ape))

cuenta = {"nombre":nom,"apellido":ape,"edad":edad,"dni":dni,"clave":clave}

i = 0

while(i!=clave):
    print(i)
    i = i+1

print(cuenta)

