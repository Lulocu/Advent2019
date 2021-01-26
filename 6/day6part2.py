

fh = open("input.txt",'r')
yo= '-'
santa ='-'
objEstelares = {}
#Saco todo lo que orbita alrededor  de cada masa
for line in fh:
    line = line.replace('\n','')
    [masa,orbitador] = line.rsplit(')')
    if orbitador == 'YOU':
        yo = masa
    elif orbitador == 'SAN':  
        santa = masa 
    objEstelares[masa] = objEstelares.get(masa,[]) + [orbitador]


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

total = 0
for key in orb.keys():
    total+= len(orb[key])

noComunes = set(orb['YOU']) & set(orb['SAN'])
listaYo = list(set(orb['YOU']) - noComunes)
listaSanta = list(set(orb['SAN']) - noComunes)
print(len(listaSanta) + len(listaYo))