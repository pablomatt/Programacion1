long1 = input('Ingrese la longitud 1 ')
long2 = input('Ingrese la longitud 2 ')
long3 = input('Ingrese la longitud 3 ')

if ((long1 < long2 + long3)and(long2< long1 + long3)and(long3 < long1 + long2)):
	print('Se forma un triangulo')
else:
	print('No se forma un triangulo')


