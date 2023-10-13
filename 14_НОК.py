#a*b=НОД*НОК

a,b = map(int, input().split())
nok=a*b
while b>0:
    a,b = b,a%b
print(nok/a)