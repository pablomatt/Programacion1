sexo = raw_input('Ingrese el sexo de la persona ')
altura = input('Ingrese la altura ')
if sexo == "femenino" and altura < 145:
	print('La mujer es petiza')
elif (sexo == "femenino") and (altura > 145 and altura < 170):
	print('La mujer es normal')
elif sexo == "femenino" and altura > 170:
	print('La mujer es alta')
elif sexo == "masculino" and altura < 160:
	print('EL hombre es petizo')
elif (sexo == "masculino") and (altura > 160 and altura < 190):
	print('El hombre es normal')
elif sexo == "masculino" and altura > 190:
	print('El hombre es alto')

