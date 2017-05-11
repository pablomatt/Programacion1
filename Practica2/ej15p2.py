import string

car = raw_input('Ingrese un caracter ')

if car in string.lowercase:
	print('@Es una MINUSCULA')
elif car in string.uppercase:
	print('@Es una MAYUSCULA')
else:
	print(' ')


