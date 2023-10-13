n = int(input())

a=[]

for i in range(n+1):
        a.append([0]*(n+1))



for i in range(n+1):
    for j in range(n+1):
        if j==0:
            a[i][j] = 1
        elif not j>i:
            a[i][j] = a[i-1][j]+a[i-1][j-1]
        elif j==i:
            a[i][j] = 1

for i in range(n+1):
    print(a[i])             
             
 