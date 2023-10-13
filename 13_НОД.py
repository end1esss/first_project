# Алгоритм Евклида
# a,b = map(int, input().split())
# while a!=b:
#     if a>b:
#         a=a-b
#     else:
#         b=b-a
# print(a)

# Оптимизированный алгоритм Евклида
# a,b = map(int, input().split())
# while b>0:
#     c=a%b
#     a=b
#     b=c
# print(a)


#Более оптимизированный алгоритм Евклида
a,b = map(int, input().split())
while b>0:
    a,b = b,a%b
print(a)