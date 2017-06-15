num1 = input('Ingrese el numero 1 ')

num2 = input('Ingrese el numero 2 ')

def max(num1, num2):

    if(num1 > num2):
        return num1
    elif(num1 == num2):
       print('Los numeros son iguales ')
    else:
        return num2

print('El maximo es %s ' %(max(num1, num2)))