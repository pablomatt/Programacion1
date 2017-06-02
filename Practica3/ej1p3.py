pal1= raw_input('Ingrese una palabra ')

pal2= raw_input('Ingrese una palabra ')

if (pal1[-3:] == pal2[-3:]):
	print('Las palabras %s y %s riman mucho' %(pal1,pal2))
elif (pal1[-2:] == pal2[-2:]):
	print('Las palabras %s y %s riman poco' %(pal1,pal2))
else:
	print('Las palabras %s y %s no riman' %(pal1,pal2))

