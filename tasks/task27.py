from math import dist
def centr(claster):
    m = []
    for point in claster:
        s = sum(dist(point, p) for p in claster)
        m.append([s, point])
    return min(m)[-1]




points = [list(map(float, p.replace(',', '.').split())) for p in open('27B_25447.txt')]

clasters = []

for point in points:
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, p) < 1 for p in claster): # смотрим на график и меняем значение, если видим, что 1 это много
            clasters[-1] += claster
            clasters.remove(claster)

cent = [centr(claster) for claster in clasters if len(claster) > 29] # зачастую кластер > 29 точек
clasters = [claster for claster in clasters if len(claster) > 29]
print(len(clasters[0]), len(clasters[1]), len(clasters[2]))
# условие
s = 0 
kol = 0
for i in range(len(clasters[1])): 
    s += dist(clasters[1][i], cent[1])
    kol += 1

print(s / (kol - 1))

#Px = min(cen[0] for cen in cent)
#Py = min(cen[1] for cen in cent)
#print(int(abs(Px) * 10000))
#print(int(abs(Py) * 10000))
print(int(sum(cen[0] for cen in cent) / len(cent)*10000))
