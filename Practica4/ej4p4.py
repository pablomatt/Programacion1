car = raw_input('Ingrese un caracter ')

ok = False

def vocal(car,ok):
    if((car == "a") or (car == "e") or (car == "i") or (car == "o") or (car == "u")):
        ok = True
    else:
        ok = False
    
    return ok

vocal(car,ok)

print(vocal(car,ok))
