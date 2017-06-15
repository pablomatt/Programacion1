num1 = input('Ingrese el numero 1 ')

num2 = input('Ingrese el numero 2 ')

num3 = input('Ingrese el numero 3 ')

def max(num1,num2):

    if(num1 > num2):
        return num1
    elif(num2 > num1):
       return num2
    else:
        return -1

max(num1,num2)

def max_de_tres(num1,num2,num3):
    aux = max(num1,num2)
    if(aux == -1):
        if aux == max(num2,num3):
            return num3   
        else:
            return max(num2,num3)
    else:
        return max(aux,num3)
            
max_de_tres(num1,num2,num3)

print('El maximo es %s ' %(max_de_tres(num1,num2,num3)))
