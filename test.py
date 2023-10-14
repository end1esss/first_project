def funtik(a: int) -> str | list:
    s = 'Hello'
    return s*a


for i in range(int(input())):
    print(funtik(i))
    print(i, end='')
