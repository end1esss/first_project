a=[0,1,2,3,2,1,1,2,4,1,2,3,4,1,0]
b=[]
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
for i in range(len(b)):
    print("i=",i,"Count=",a.count(i))


d=[0,2,2,4,2,1,1,2,4,1,1,3,4,1,0,1,4,4,4,0] #ограниченное множество от 0 до 5 не включительно
count=[0]*5

for i in d:
    count[i]+=1

print(list(range(5)),count,sep='\n')
for i in range(5):
    print((str(i)+' ')*count[i], end='')
print(d.sort())
