# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

# 11. Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.





# _________________________________________________________________________________________________

# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
# 0! = 1 Решить задачу используя цикл while

def Task9():
    n = int(input("Input n: "))
    fact = 1
    while n >= 0:
        fact *= n
        n -= 1
        if n == 0:
            print(fact)
            break
    else:
      print(1)

# _______________________________________________________________________________

# 11. Дано натуральное число A > 1. Определите, каким по счету числом 
# Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.

def Task11_2():
    a = int(input("Input A: "))
    fiba = 0
    fibb = 1
    count = 2
    while fibb < a:
        fibc = fiba + fibb
        fiba = fibb
        fibb = fibc
        count += 1
    if a != fibb:
        print(-1)
    else:
        print(count)

# _________________________________________________________________________________

# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями 
# статистики за прошлые годы. Их интересует, сколько дней длилась 
# самая длинная оттепель. Оттепелью они называют период, в который 
# среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.  Пользователь
# вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.  Каждое число – среднесуточная 
# температура в соответствующий день. Температуры – целые числа
# и лежат в диапазоне от –50 до 50

def Task13():
    len = int(input("Input count of days: "))
    temper = list()
    for _ in range(0, len):
        temper.append(int(input()))
    print(temper, end=' ')
    temper.append(-5)
    count = 0
    max = 0
    for i in temper:
        if i > 0:
            count += 1
        else:
            if max <= count:
                max = count
            count = 0
    print(max)
# ______________________________________________________________________________

# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: 
# один для себя, а другой для тещи. Понятно, что для себя нужно
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать самый легкий
# и самый тяжелый арбуз? Помогите ему! 
# Пользователь вводит одно число N – количество арбузов. Вторая
# строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все
# числа натуральные и не превышают 30000.

def Task15():
    len = int(input("Input count of arbuzes: "))
    arbuzes = list()
    for _ in range(0, len):
        arbuzes.append(random.randint(1, 10))
    print(arbuzes)
    min = arbuzes[0]
    max = min
    for el in arbuzes:
        if el < min:
            min = el
        if el > max:
            max = el
    print(min , max)

# Вводится два числа а и б, найти все простые числа в диапозоне

# def ATask():
#     a = int(input("Input A: "))
#     b = int(input("Input B: "))
#     eazy = list()

#     for i in range(2, 6):
#             if a % i == 0:
#                 break
#         else:
#             eazy.append(a)
#     a += 1
#     print(eazy)