from random import randint

count=0

a = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&()*+,-./:;<=>?@[\]^_`{|}~♂♀'

password = a[randint(0,94)] + a[randint(0,94)] + a[randint(0,94)]

print('Secret Password:',password)

for first in a:
    for second in a:
        for third in a:
            count+=1
            password_try = third+second+first                         
            if password_try==str(password):
                print("Success! Count = ",count)
                break