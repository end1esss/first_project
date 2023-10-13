n = int(input())
m = int(input())
sam=n
sMamoi = 0
while n//m>=1:
    sMamoi=sMamoi+n//m
    print(sMamoi)
    n=n//m
    print(n)
print(sam+sMamoi)