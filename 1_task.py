gender = {
    'м': 'Дорогой',
    'ж': 'Дорогая'
}

a = [
    ['Марина','Абрамовна',34,'ж'],
    ['Пётр','Абрамович',1231,'м']
]

for n,s,b,g in a:
    print(f"{gender[g]} {n+' '+s}. У вас осталось на счёте {b} долларов. Пополните, пожалуйста счёт для дальнейшего списания средств")