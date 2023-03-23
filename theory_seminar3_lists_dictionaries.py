# ТЕОРИЯ. СПИСКИ И СЛОВАРИ

# СПИСКИ - тип данных list, в списке могут быть разные типы данных
# some_list = [1, '1', True, [1, 2], {1: 2}]
# print(some_list)
# some_list.append(10) # добавление элемента в конец списка
# print(some_list)
# some_list.insert(3, 100) # добавление элемента на определенную позицию  (индекс, элемент)
# print(some_list) 

# some_list = [1, '1', True, [1, 2], {1: 2}]
# for el in some_list: # по списку можем проходить циклом for
#     print(el)

# КОРТЕЖ - неизменяемый список, нет методов для добавления или удаления элементов.
# Можно из списка делать кортеж, и наоборот.

# some_tuple = (1, 2, 3, 4, 5)
# some_list = list(some_tuple) # кортеж в список
# print(some_list)

# МНОЖЕСТВА
# по сути это список, но содержит только уникальные элементы.
# В множестве нет порядка. Следовательно, нет индексов.
# some_set = {1, 2, 5, 7, 7, 9}
# print(some_set) # будет только одна 7. Вывод: {1, 2, 5, 7, 9}

# Создадим некоторый список.
# И списки, и множества, и кортежи можно создавать в одну строчку
# с помощью так называемых списочных выражений.

# import random

# Запись с помощью цикла:
# some_list = [] # создадим пустой список
# for _ in range(100):
#     some_list.append(random.randint(1, 50))

# Эквивалентная запись в строку:
# some_list = [random.randint(1, 50) for _ in range(100)] 
# заполним список рандомными элементами
# внутри квадратных скобок записываем правило, по которому будет формироваться список
# сто раз сгенирируем рандомный элемент от 1 до 50 и добавим его в наш список
# start = time.perf_counter()
# print(40 in some_list)
# end = time.perf_counter()
# print(end - start)

# Как примерно реализована с помощью цикла операция in (если бы писали на Python):
# for i in some_list:
#     if i == 40:
#         print(True)
#         break
# else:
#     print(False)

# some_set = [random.randint(1, 50) for _ in range(100)] # тоже со множеством
# start = time.perf_counter()
# print(40 in some_set)
# end = time.perf_counter()
# print(end - start)

# СЛОВАРИ (ключи - неизменяемый тип данных)
# some_dict = {'name': 'Alex', 'surname': "Salnikov"}
# print(some_dict)

# some_dict = {frozenset({1, 2, 3}): 'Alex', 'surname': "Salnikov"}
# print(some_dict)

# типы данных:
# Неизменяемые: int, str, float, bool, turple, frozenset
# Изменяемые: set, list, dict

some_dict = {'name': 'Alex', 'surname': "Salnikov", 123: [1, 2, 3]}
# print(some_dict['name']) # поиск элемента по индексу

# some_dict['age'] = 21 # дополнение словаря (новый ключ и значение)
# print(some_dict)

# print(some_dict['address']) # запрос ключа, которого нет. Вывод: KeyError: 'address'

# если надо, чтобы программа дальще работала, то метод get
# print(some_dict.get('address')) # Вывод: None
# print(some_dict.get('address', 'Такого ключа нет')) # Вывод: Такого ключа нет

# print(some_dict.values()) # список значений
# print(some_dict.keys()) # список ключей
# print(some_dict[123][0]) # запрос элемента по индексу [0] из списка с ключом 123. Вывод: 1

# a = [1, 2, [3, 4, [5, 6]]] # список внутри списка, хотим вытащить 5
# print(a[2][2][0]) # Вывод: 5

# ИЗМЕНЕНИЕ ЭЛЕМЕНТОВ ВНУТРИ СПИСКА:
a = [1, 2, 3] # список из строк, надо сделать числовой список
for ind in range(0, len(a)):
    a[ind] = int(a[ind])
print(a)


# ДЛЯ СЕБЯ: (задача 16)
# input_list = [int(i) for i in input().split()] #заполним список метод split
# # Метод .split() разделяет основную строку по разделителю и возвращает список строк.
# input_x = int(input()) 
# print(input_list.count(input_x))




