# Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

# # СПОСОБ 1
# input_list = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len): 
#     input_list.append(int(input(f"Введите число: ")))
# print(input_list)

# input_x = int(input("Заданное число X: "))

# b=[abs(input_list[i]-input_x) for i in range(len(input_list))]
# print(input_list[b.index(min(b))])

# # СПОСОБ 2
# input_list = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len): 
#     input_list.append(int(input(f"Введите число: ")))
# print(input_list)

# input_x = int(input("Введите число X: "))

# print(min(input_list, key=lambda a:abs(a-input_x)))

# # Комментарий: Встроенная функции min с необязательным аргументом key,
# # который принимает функцию определяющую порядок сравнения элементов.
# # Элементы сравниваются между собой по абсолютной разнице между ними и заданным значением.
# # То есть меньшим будет тот, у которого эта разница меньше.

# РАЗБОР НА СЕМИНАРЕ:
import time
import random
from random import randrange
from time import perf_counter

some_list = [random.randint(-100, 100) for _ in range(10)]
print(some_list)
x = int(input())

start = perf_counter()
some_set = set(some_list)

diff = 1
while True:
    if x + diff in some_set:
        print(x + diff)
        break
    elif x - diff in some_set:
        print(x - diff)
        break
    diff += 1
end = perf_counter()
print(end - start)