import  numpy
sorozat = []
a = 1
c = []
for i in range(1,192):
    b = []
    for j in range(1,i):
        b.append(i-1)
    c.extend(b)

print(c)
print(c.count(190))

print(numpy.median(c))