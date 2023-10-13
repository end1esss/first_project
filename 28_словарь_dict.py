a = [['moskva',495], ['piter',812], ['penza',8412]]

# 'moskva' - 495,
# 'piter' - 812,
# 'penza' - 8412

#1 способ
d = {
    'moskva': 495,
    'piter': 812,
    'penza': 8412
}
#2 способ словаря/функция dict/работает только со строками
r = dict(moskva=495,piter=812,penza=8412)

#3 через вложенные списки с функцией dict

t = dict(a)
print(t)

# если хотим проинициализировать наши ключи определенным значением

q = dict.fromkeys(['a','b','c'],10)

# удаление ключа

del d['moskva']

#функции со словарями

print(len(d))

if 5 in d:
    print(d[5])
else: 
    d[5] = 'five'

for key in d:
    print(key, d[key])

#методы со словарями
d.clear()
print(d.get(1,'Get the fuck out here')) #передаёт значение из ключа. Если ключа нет - можно указать, 2ой параметр который будет выводиться вместо None
print(d.setdefault(7,'seven')) #передаёт значение ключа и добавляет в словарь если данного ключа нет
print(d.pop(3)) #выводит значение и удаляет из словаря
print(d.popitem) #выведет пару и удалит из словаря рандомно

print(d.keys) #только ключи
print(d.values) #только значения
print(d.items) #возвращает пары ключ - значение

for key,value in d.items:
    print(key, value)