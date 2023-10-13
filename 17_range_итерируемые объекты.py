print(list(range(10)))
print(len(list(range(10))))
print(list(range(1,10)))
print(list(range(1,10,2)))
print(list(range(10,0,-1)))
print(sum(range(1,5)))
a,b,c = range(4,7)
print(a,b,c)

v=iter(range(5)) #позволяет поочередно проходить по элементам, запоминая на каком мы остановились
print(next(v))
print(next(v))

n=iter([43,True,'hi'])
print(next(n))
print(next(n))
print(next(n))

m=iter('hi')
print(next(m))
print(next(m))
