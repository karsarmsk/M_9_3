first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# В переменную  разница длин                 из списков    если длины не равны
first_result = (len(x)-len(y) for x,y in zip(first, second) if len(x) != len(y))
print(list(first_result))
# в переменную      сравнение длин строк      в одной позиции   длина одинаковая
second_result = (len(first[i]) == len(second[i]) for i in range(len(second)))
print(list(second_result))