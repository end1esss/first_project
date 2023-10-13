a = []

s = int(input()) 

for i in range(s):
    a.append([0]*s)

for i in range(s):
    for j in range(s):
        if i>j:
            a[i][j]=1
        elif i==j:
            a[i][j]=0
        else:
            a[i][j]=3

for i in a:
    print(i)
        