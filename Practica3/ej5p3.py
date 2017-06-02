fin = False

lista_dias = []

max = 0

min = 9999999

dia_nom_max = ""

dia_num_max = 0

dia_nom_min = ""

dia_num_min = 0


while(not fin):
    clima = {}
    clima["temperatura"] = input('Ingrese una temperatura ')
    clima["humedad"] = raw_input('Ingrese el porcentaje de la humedad ')
    clima["plluvia"] = input('ingrese el porcentaje de la probabilidad de lluvias ')
    clima["vel_viento"] = input('Ingrese la velocidad del viento ')
    clima["dir_viento"] = raw_input('ingrese la direccion del viento ')
    clima["nom_dia"] = raw_input('Ingrese el nombre del dia ')
    clima["num_dia"] = input('Ingrese el numero del dia ')
    clima["hora"] = input('Ingrese la hora ')
    lista_dias.append(clima)

    if(clima["temperatura"]>max):
        max = clima["temperatura"]
        dia_nom_max = clima["nom_dia"]
        dia_num_max = clima["num_dia"]

    if(clima["plluvia"]<min):
        min = clima["plluvia"]
        dia_nom_min = clima["nom_dia"]
        dia_num_min = clima["num_dia"]

    print('Persona agregada')
    fin = input('Finalizar:1, Continuar:0 ')

print('Lista de personas agregadas: ')
print(lista_dias)
print('El dia con mayor temperatura fue %s %s' %(dia_nom_max,dia_num_max))
print('El dia con menores probabilidades de lluvia fue %s %s' %(dia_nom_min,dia_num_min))
