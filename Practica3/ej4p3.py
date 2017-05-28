fin = False

lista_dias = []

while(not fin):
    clima = {}
    clima["temperatura"] = input('Ingrese una temperatura ')
    clima["humedad"] = raw_input('Ingrese el porcentaje de la humedad ')
    clima["plluvia"] = raw_input('ingrese el porcentaje de la probabilidad de lluvias ')
    clima["vel_viento"] = input('Ingrese la velocidad del viento ')
    clima["dir_viento"] = raw_input('ingrese la direccion del viento ')
    clima["nom_dia"] = raw_input('Ingrese el nombre del dia ')
    clima["num_dia"] = input('Ingrese el numero del dia ')
    clima["hora"] = input('Ingrese la hora ')
    lista_dias.append(clima)
    print('Persona agregada')
    fin = input('Finalizar:1, Continuar:0 ')

print('Lista de personas agregadas: ')
print(lista_dias)

