set1={2,4,5,6,6,6,8,8,9}
print(set1)
set1.add(10)
print(set1)
set2={0,1,2,3,4,6}
inter=set1.intersection(set2)
print(inter)
un=set1.union(set2)
print(un)
dif=set1.difference(set2)
print(dif)
sim=set1.symmetric_difference(set2)
print(sim)
set2.pop()
print(set2)