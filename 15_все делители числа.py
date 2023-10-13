n = int(input())
i=1
a=[]
while i<=n**0.5:
    if n%i==0:
        a.append(i)
        if i!=n//i:
            a.append(n//i)
    i=i+1
a.sort()    
print(a)