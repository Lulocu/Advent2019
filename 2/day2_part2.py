"""
Advent of code 2019 day 2
""" 
#mapeos
parar = 99
sumar = 1
multiplicar = 2
#variable respuesta encontrada
terminar = False

#Para no perder datos originales
fh = open("input.txt",'r')
origen = fh.read()
origen = origen.rsplit(',')
fh.close()
origen = list(map(int,origen))

for noun in range(0,100):
    if terminar:
        break
    for verb in range(0,100):
        if terminar:
            break

        #para no alterar la lista original
        datos = origen.copy()
        datos[1] = noun
        datos[2] = verb
        
        
        for i in range(0,len(datos),4):
        
            if datos[i] == parar:
                break
            
            elif datos[i] == sumar:
                datos[datos[i+3]]  = datos[datos[i+1]] + datos[datos[i+2]]
        
            elif datos[i] == multiplicar:
                datos[datos[i+3]]  = datos[datos[i+1]] * datos[datos[i+2]]
        
            else:
                raise Exception('Code op at position %f is not correct. CodeOp = %f',i,datos[i])

        if datos[0] == 19690720:
            terminar = True
            print('fin')
            break
#Por el desajuste de entrar una vez de más en el bucle  de noun
print(100*(noun-1)+verb)
