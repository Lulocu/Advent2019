"""
Advent of code 2019 day 2
""" 
#mapeos
parar = 99
sumar = 1
multiplicar = 2

fh = open("input.txt",'r')

datos = fh.read()
datos = datos.rsplit(',')

datos[1] = 12
datos[2] = 2
datos = list(map(int,datos))

for i in range(0,len(datos),4):

    if datos[i] == parar:
        break

    elif datos[i] == sumar:
        datos[datos[i+3]]  = datos[datos[i+1]] + datos[datos[i+2]]

    elif datos[i] == multiplicar:
        datos[datos[i+3]]  = datos[datos[i+1]] * datos[datos[i+2]]

    else:
        raise Exception('Code op at position %f is not correct. CodeOp = %f',i,datos[i])

print(datos[0])
