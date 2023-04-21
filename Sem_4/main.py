# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# sp = input().split()
# result = ()

# for i in sp:
#     if i in result:
#       print(f'{i}_{result[i]}', end = " ")
#       result[i] = result[i]+1
#     else:
#       print(i, end = " ")
#       result[i] = 0

import random

some_str = ''.join([chr(random.randint(32, 100)) for _ in range(10 ** 5)])

import time
start = time.perf_counter()
for letter in set(some_str):
    a = letter, some_str.count(letter)
end = time.perf_counter()
duration1 = end - start

start = time.perf_counter()
for letter in set(some_str):
    amount = 0
    for letter1 in some_str:
        if letter == letter1:
            amount += 1
    a = letter, amount
end = time.perf_counter()
duration2 = end - start
# print(duration2 / duration1)

start = time.perf_counter()
count = 0
lens = len(some_str)
while lens > 0:
    for i in range(0, lens):
        if some_str[0] == some_str[i]:
            count += 1
    lens -= count
    a = f'{some_str[0]} -> {count}'
    some_str = some_str.replace(some_str[0], '')
    count = 0
end = time.perf_counter()
duration3 = end - start


start = time.perf_counter()
count_dict = {}  # a: 1
for letter in some_str:
    if letter not in count_dict:
        count_dict[letter] = 1
    else:
        count = count_dict[letter]
        count_dict[letter] = count + 1
end = time.perf_counter()
duration4 = end - start
print(duration1, duration2, duration3, duration4)