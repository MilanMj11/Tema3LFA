file = open("input.txt",'r')
lungime_cuvant = int(file.readline())
gramatica = {} # dictionarul gramaticii
for line in file.readlines():
    List = line.strip().split()
    n = len(List)
    stare = List[0]
    aux = []
    for i in range(2,n,2):
        if(List[i] == '_') :
            List[i] = ''
        aux.append(List[i])
    gramatica[stare] = aux
#print(lungime_cuvant)
#print(gramatica)

optiuni = []
for optiune in gramatica['S']:
    optiuni.append(optiune)
pas = 1
#print(gramatica)
#print(optiuni)
posibile_raspunsuri = []
while pas < lungime_cuvant:
    aux = []
    for optiune in optiuni:
        lungime_optiune = len(optiune)
        poz_litera_mare = -1
        for i in range(lungime_optiune):
            if optiune[i].isupper() == True:
                poz_litera_mare = i
                break
        # acum inlocuiesc litera mare cu fiecare drum din gramatica
        if poz_litera_mare == -1 :
            posibile_raspunsuri.append(optiune)
            continue
        litera_mare = optiune[poz_litera_mare]
        prima_parte = optiune[:poz_litera_mare]
        doua_parte = optiune[poz_litera_mare+1:]
        for drum in gramatica[litera_mare]:
            # vreau sa inlocuiesc litera mare cu drumul
            nou_cuvant = prima_parte + drum + doua_parte
            aux.append(nou_cuvant)
        for cuvant in aux:
            if len(cuvant) == lungime_cuvant:
                posibile_raspunsuri.append(cuvant)
    optiuni = aux
    #print(optiuni)
    pas += 1
#print(optiuni)
#print(posibile_raspunsuri)
raspunsuri = set()
for cuvant in posibile_raspunsuri:
    ok = True
    if len(cuvant) != lungime_cuvant :
        continue
    for litera in cuvant:
        if litera.isupper() or litera=='_':
            ok = False
            break
    if ok == True:
        raspunsuri.add(cuvant)
for rasp in raspunsuri:
    print(rasp)
