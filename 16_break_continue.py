while True:
    a = input()
    if a =='exit':
        break
    if a.isdigit():
        print("Попробуй ввести не число а слово")
        continue
    print("Длина слова: ",len(a))
print("Вы вышли из программы")