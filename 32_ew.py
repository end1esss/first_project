phrases = []

# Считываем фразы по одной и добавляем их в список
while True:
    phrase = input("Введите фразу (для завершения введите 'конец'): ")
    if phrase.lower() == 'конец':
        break
phrases.append(phrase)

# Воспроизводим фразы в обратной последовательности
print("Фразы в обратной последовательности:")
for phrase in reversed(phrases):
    print(phrase)