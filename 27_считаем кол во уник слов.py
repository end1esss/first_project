text = input()
a = set()
while text!='':
    a.update(set(text.split()))
    text = input()
print(a)
print(len(a))