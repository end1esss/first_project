a = int(input())
b = list(map(int, input().split()))
count = 0
for i in range(a-1):
    for k in range(a-1-i):
        if b[k] > b[k+1]:
            count += 1
            b[k], b[k+1] = b[k+1], b[k]
        # print(b)
print(*b)
print(count)
