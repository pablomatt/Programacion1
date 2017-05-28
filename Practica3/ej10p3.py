import random

finalizar = False

num = input('Ingrese un numero ')

random.randint(0,num+1)

if(num < 4):
    print('Easy')
elif ((num <= 8) and (num > 4)):
    print('Medium')
elif ((num <= 16) and (num > 8)):
    print('Hard!')

while(not finalizar):
    