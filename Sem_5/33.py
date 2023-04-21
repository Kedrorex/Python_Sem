# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random 

number_list = int(input("Введите количтсво оценок: "))
some_list = [random.randint(1, 5) for i in range (number_list)]

min = max = some_list[0]

for i in some_list:
    if min > i:
          min = i
    elif max < i:
          max = i

print(*some_list)

for i in range (len(some_list)):
    if some_list[i] == max:
        some_list[i] = min

print(*some_list)