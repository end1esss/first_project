b={}
d = {
    1: 45,
    'hello': 'two',
    3: [1,2,3]
}
d[4] = 'seq' #можно вне списка создать пару ключ - значение
print(d[1]) #словарь[ключ]



person = {}
s = "Ivanov Ivan Samara SGU 5 3 3 5 3 2 3 4"
s = s.split()
person['lastName'] = s[0]
person['firstName'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
for i in s[4:]:
    person['marks'].append(int(i)) 
print(person)