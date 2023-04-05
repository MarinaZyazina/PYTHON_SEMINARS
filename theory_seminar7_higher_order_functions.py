# Функции высшего порядка (higher order functions): map, filter, zip, lambda, enumerate


# пример использования map:

# def square(a):
#     return a ** 2

# some_list = [1, 2, 3, 4, 5]
# print(list(map(square, some_list))) # Вывод: [1, 4, 9, 16, 25]. 
# # P.S. map создает новый объект, и мы его куда-то записываем.

# # Это тоже самое, что:
# some_list = [1, 2, 3, 4, 5]
# for i in range(len(some_list)):
#     some_list[i] = some_list[i] ** 2
# print(some_list) # Вывод: [1, 4, 9, 16, 25]
# # P.S. Изменения происходят в старом объекте.



# пример использования lambda (на предыдущем примере):
# some_list = [1, 2, 3, 4, 5]
# print(list(map(lambda a: a ** 2, some_list))) # Вывод: [1, 4, 9, 16, 25]



# пример использования filter (похожа на map, map - функция, filter - условие):
# some_list = [1, 2, 3, 4, 5]
# print(list(filter(lambda x: x % 2 == 0, some_list))) # Вывод: [2, 4]



# пример использования zip:
# some_list = [1, 2, 3, 4, 5]
# some_list2 = {'1', '2', '3', '4', '5'}
# print(list(zip(some_list, some_list2))) # [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
# Объединяет поочередно элементы с 1-го и 2-го списка в кортеж. 
# Выстраивается по минимальному количеству элементов в к.-л. из списков
# Использовать для вывода, объединения:
# for i, j in (zip(some_list, some_list2)):
#     print(i, j)
# # Вывод:
# # 1 1
# # 2 2
# # 3 3
# # 4 4
# # 5 5



# пример использования enumerate:
some_list = [1, 2, 3, 4, 5]
print(list(enumerate(some_list))) # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# Первый элемент полученного кортежа - индекс, второй - значение из списка

