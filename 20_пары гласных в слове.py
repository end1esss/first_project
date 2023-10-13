vowels = 'aeiou'
t = str(input())

for i in range(len(t)-1):
    if t[i] in vowels and t[i+1] in vowels:
        print(t[i],t[i+1])