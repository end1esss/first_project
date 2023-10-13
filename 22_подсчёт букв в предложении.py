a = str(input())

letters = [0]*26

for i in a.lower():
    if i>='a' and i<='z':
        letters[ord(i)-97]+=1

for i in range(26):
    if letters[i]!=0:
        print(chr(i+97),letters[i],sep='=',end=' ')