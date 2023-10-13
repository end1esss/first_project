guess = int(input())
password = 123
while guess!=password:
    print('Wrong password')
    guess = int(input())
print('Success')