

fh = open("inputPrueba.txt",'r')

objEstelares = {}
#Saco todo lo que orbita alrededor  de cada masa
for line in fh:
    line = line.replace('\n','')
    [masa,orbitador] = line.rsplit(')')
    objEstelares[masa] = objEstelares.get(masa,[]) + [orbitador]

#Recorro las masas que orbitan empezando por COM
#Hago un diccionario que dice COM orbita alrededor de nada
#A orbita alrededor de COM
#C orbita alrededor de A y COM

inicial = ['COM']
orb = {}
orb['COM'] = []
while len(inicial) > 0:
    centroActual = inicial.pop(0)
    orbitas = objEstelares.get(centroActual,None)
    if orbitas is not None:
        inicial = inicial + orbitas
        for elemento in orbitas:
            orb[elemento] =  orb.get(centroActual,[]) + [centroActual] + orb.get(elemento,[])
#sumo las longitudes de los valores  de los diccionarios
total = 0
for key in orb.keys():
    total+= len(orb[key])