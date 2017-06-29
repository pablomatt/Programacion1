vidas = 10

gane = False

pal = raw_input("Ingrese una palabra ")

res = []

def reemplazo(pal,letra,res):
    pos = []
    i = 0
    check = False
    for k in pal:
        if k == letra:
            check = True
            res.append(k)
        else:
            res.append("_")
    print(res)
    return check

while((gane == False) and (vidas > 0)):
    letra = raw_input('Ingrese una letra ')
    if(len(letra) == 1):
        j = reemplazo(pal,letra,res)
        