semana=["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]

i=input('Ingrese un numero del 1 al 7 ')

if i>0 and i<=7:
	print('El dia de la semana elegido es %s ' %(semana[i-1]))
	print (i)
else:
	print('El numero ingresado es incorrecto')
