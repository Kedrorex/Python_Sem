# Дан список интов
# повторяющихся
# элементов
# в списке нет.
# Нужно преобразовать это множество в строку,
# сворачивая соседние по числовому ряду числа
# в диапазоны.
# Примеры

# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

import random

number = int(input("Введите количтсво оценок: "))
number_spisok = [random.randint(0, 10) for i in range (number)]

print(number_spisok)
number_spisok = sorted(number_spisok)
set_list = set(number_spisok)
number_spisok = list(set_list)
print(number_spisok)

spec_list = list()
temp_list = list()

if number_spisok[1] - number_spisok[0] != 1:
    temp_list.append(number_spisok[0]) 

for i in range(1, len(number_spisok)):
    if number_spisok[i] - number_spisok[i-1] == 1:
        spec_list.append(number_spisok[i])
    elif spec_list != 0:
        temp_list.append(spec_list)
        spec_list = 0
    else:
        temp_list.append(number_spisok[i])

print(temp_list)