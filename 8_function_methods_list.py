marks=[4,5,4,3,2,4,5,4]
a=[True,43,'helloo',5.4,[4,5,6]]
len(a) #5 элементов

a = a + [4] #добавили элемент в список
a = a * 4 # продублировали 4 раза список

max(marks) #max чисел
min(marks) #min чисел
sum(marks) #сумма чисел
sorted(marks) #по возрастанию
sorted(marks,reverse = True) #по убыванию
sum(marks)/len(marks) #ср арифмет

a = [12,42,123,451,18,65]
a.append(22) #add to end new number or list [1,2,3] or string 'key'
print(a)
b = [1,2,3,4,5]
b.clear() #clear list
c = [1,2,3,4]
d = c.copy() #copy list, same values but links in different object
e = c[:] #full srez of list, all elements
print(d)

c.count(2) #count definite elements in list
c.index(3) #find index of value
c.index(2,1,3) #where 2 - our value, from number with index 1 to 3 
c.insert(2,100) #add on second index number 100
c.pop() #delete last element and show this one on screen
c.delete(2) #delete value
c.reverse() #reverse list
c.sort() #sort from min to max
c.sort(reverse=True) #sort from max to min