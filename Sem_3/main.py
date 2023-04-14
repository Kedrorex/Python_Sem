some_str = 'hello'

# for ind in range (0, len(some_str)):
#     print(some_str[ind])

# print(some_str[::-1]) # перевернутая строка

# СПИСКИ

# some_str = [1, 'fbs', True, [1,2,3], {5,4,2}]

# some_str = []
# for _ in range(10):
#     number = int(input())
#     some_str.append(number)
# print(some_str)

# some_list = [int(input() for _ in range(10))]
# print(some_list)

# some_list = [random.randint(1, 10) for _ in range(10))]
# print(some_list)

# print(some_list.count(7)) # Выведет количство 7 в списке

# print(7 in some_list) # Выведет тру или фальс

# КОРТЕЖ и Множества

# import random
# import time
# some_list = [random.randint(1, 10000) for i in range(10 ** 7)]
# some_set = set(some_list)
# some_list = list(some_set)

# start = time.perf_counter()
# print(11000 in some_list)
# end = time.perf_counter()
# duration1 = end - start

# start = time.perf_counter()
# print(11000 in some_set)
# end = time.perf_counter()
# duration2 = end - start

# print(duration1 / duration2)

# ___________________________________________________________________
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# num = list(map(int, input().split()))
# num = [1, -1, 2, 0, 1, 3, 4, 4]
# num = list(map(int, input().split()))
# num = set(num)
# print(num, len(num))


# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.

# array1 = [1, 2, 3, 4, 5]
# k = 3
# for i in range(k):
#     for j in range(len(array1)):
#         # temp = array1[j]
#         # array1[j] = array1[-1]
#         # array1[-1] = temp
#         array1[j], array1[-1] = array1[-1], array1[j]

# print(array1)
# array1 = [1, 2, 3, 4, 5]
# k = 2
# part1 = array1[-k:]
# print(part1)
# part2 = array1[:-k]
# print(part2)
# array1_2 = part1 + part2
# print(array1_2)

# Напишите программу для печати всех уникальных значений в словаре.

# dict_1 = {"V": "S001", "V": "S002", "VI": "S001",
#           "VI": "S005", "VII": " S005 ", " V ": " S009 ",
#           " VIII": " S007 "}

# a = set()
# for i in dict_1.values():
#     a.add(i)
# print(a)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номеро

# ist_1 = [0, -1, 5, 2, 3, 1, 2, 0]

# def STask23():
#     listn = list()
#     for i in range(0, 10):
#         listn.append(random.randint(-10, 10))
#     print(listn)
#     listt = list()
#     count = 0
#     for i in range(len(listn)-1):
#         if listn[i] < listn[i + 1]:
#             count += 1
#             listt.append(f'{listn[i]} < {listn[i + 1]}')
#     print(f'{count} {listt}')
# STask23()

# https://www.dropbox.com/s/7n18ccc3dgxf8u9/workbook.pdf?dl=0