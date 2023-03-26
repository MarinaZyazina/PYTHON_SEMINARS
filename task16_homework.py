# Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X. 
# Попробуйте использовать метод count(), а 
# также решите задачу с помощью своего алгоритма (без count). 
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

# # СПОСОБ 1 (с использованием метода count())
# input_list = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len): 
#     input_list.append(int(input(f"Введите число: ")))
# print(input_list)

# input_x = int(input("Введите число X: "))

# print(input_list.count(input_x))


# # СПОСОБ 2
# input_list = []
# list_len = int(input("Введите количество элементов в массиве: "))
# for _ in range(list_len): 
#     input_list.append(int(input(f"Введите число: ")))
# print(input_list)

# input_x = int(input("Введите число X: "))

# count = 0
# for i in range(list_len): 
#         if input_x == input_list[i]: 
#             count += 1
# print(f"Число встречается в массиве {count} раз/а")

# РАЗБОР НА СЕМИНАРЕ 4:
import time
import random
some_list =[random.randint(1, 10000) for _ in range(10 ** 6)]
x = int(input())

start = time.perf_counter()
print(some_list.count(x))
end = time.perf_counter()
first = end - start

start = time.perf_counter()
amount = 0
for el in some_list:
    if el == x:
        amount += 1
print(amount)
end = time.perf_counter()
second = end - start

print(second / first)