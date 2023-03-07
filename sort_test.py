import datetime

l = [('a',datetime.datetime(2021,10,13),'1'), ('b',datetime.datetime(2020,1,1),'2')]

m =sorted(l, key=lambda x: x[1])

print(str(l))
print(str(m))
