from collections import Counter
valem = "CH3(CH2)3ONa + O2 -> CO2 + H2O"
valem2 = "I{-} + Cu{2+} -> CuI + I2"
def pooled(valem):
    valem = valem.replace("→", "=").replace("->", "=").split("=")
    return valem[0].strip().split(" + "), valem[1].strip().split(" + ")

def summaarne(valem, c=1):
    sum = {}
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
            sum = dict(Counter(sum) + Counter(summaarne("".join(järgmine), n*c)))
            järgmine = []
        elif element != "":
            if element not in sum:
                sum[element] = 0
            sum[element] += n*c
        
        if valem[i] == "(":
            sulud += 1
            continue
        element = valem[i]
        n = 1
        
    if järgmine != []:
        sum = dict(Counter(sum) + Counter(summaarne("".join(järgmine), n*c)))
    elif element != "":
        if element not in sum:
            sum[element] = 0
        sum[element] += n*c
        
    return sum

print(pooled(valem))
for i in pooled(valem):
    for j in i:
        print(j, summaarne(j))