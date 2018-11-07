def pooled(valem):
    valem = valem.replace("→", "=").replace("->", "=").split("=")
    return valem[0].strip().split(" + "), valem[1].strip().split(" + ")

def summaarne(valem, elist, c=1):
    sum = [0]*len(elist)
    element = ""
    järgmine = []
    sulud = 0
    n = 1
    for i in range(len(valem)):
        if valem[i].islower():
            element = element + valem[i]
            continue
        
        if sulud > 0:
            if valem[i] == "(":
                sulud += 1
            elif valem[i] == ")":
                sulud -= 1
                if sulud == 0:
                    continue
            järgmine.append(valem[i])
            continue           
        if valem[i].isnumeric():
            if valem[i-1].isnumeric():
                n = 10*n + int(valem[i])
            else:
                n = int(valem[i])
            continue
        
        if järgmine != []:
            rsum = summaarne("".join(järgmine), elist, n*c)
            for j in range(len(elist)):
                sum[j] = sum[j] + rsum[j]
            järgmine = []
        elif element != "":
            for j in range(len(elist)):
                if element == elist[j]:
                    sum[j] += n*c
        
        if valem[i] == "(":
            sulud += 1
            continue

        element = valem[i]
        n = 1
        
    if järgmine != []:
        rsum = summaarne("".join(järgmine), elist, n*c)
        for i in range(len(elist)):
            sum[i] = sum[i] + rsum[i]
    elif element != "":
        for i in range(len(elist)):
                if element == elist[i]:
                    sum[i] += n*c
        
    return sum

def elemendid(valem):
    el = []
    c = 0
    for i in range(len(valem)):
        if valem[i].isalpha():
            if valem[i].islower():
                el[c-1] = el[c-1] + valem[i]
            else:
                el.append(valem[i])
                c += 1
    return list(set(el))

def komp_maatriks(valem):
    elist = elemendid(valem)
    maatriks = []
    for i in pooled(valem):
        for j in i:
            maatriks.append(summaarne(j, elist))
    return maatriks

def mvis(km,valem):
    print(" "*19, elemendid(valem))
    for i,j in zip(km, pooled(valem)[0] + pooled(valem)[1]):
        print('{:<20}{}'.format(j, i))
        
def tasakaalustatud(c, valem):
    valem = pooled(valem)
    return " = ".join([" + ".join([str(abs(c[i]))+valem[0][i] for i in range(len(valem[0]))]), " + ".join([str(abs(c[len(valem[0])+i]))+valem[1][i] for i in range(len(valem[1]))])])
