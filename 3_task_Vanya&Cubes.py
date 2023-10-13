value = int(input())
i: int | str
sum = 0
i = 0
j = 1
while value >= sum:
    i = i+j
    j = j+1
    sum = sum+i
print(j-2)
