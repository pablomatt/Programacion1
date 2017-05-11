import string
rango = string.lowercase[:] + string.uppercase[:]
car = raw_input('Ingrese un caracter ')


if car in string.letters:
	print('El caracter %s es una letra ' %(car))
elif car in string.digits:
	print('El caracter %s es un digito ' %(car))
else:
	print('El caracter %s es un caracter especial ' %(car))


