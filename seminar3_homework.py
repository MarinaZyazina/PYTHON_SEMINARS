# ЗАДАЧА 16.
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

# # Способ 1 (с использованием метода count())
input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len): 
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_x = int(input("Введите число X: "))

print(input_list.count(input_x))

# Способ 2
input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len): 
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_x = int(input("Введите число X: "))

count = 0
for i in range(list_len): 
        if input_x == input_list[i]: 
            count += 1
print(f"Число встречается в массиве {count} раз/а")

# ЗАДАЧА 18.
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

# Способ 1
input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len): 
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_x = int(input("Заданное число X: "))

b=[abs(input_list[i]-input_x) for i in range(len(input_list))]
print(input_list[b.index(min(b))])

# Способ 2
input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range(list_len): 
    input_list.append(int(input(f"Введите число: ")))
print(input_list)

input_x = int(input("Введите число X: "))

print(min(input_list, key=lambda a:abs(a-input_x)))
# Комментарий: Встроенная функции min с необязательным аргументом key,
# который принимает функцию определяющую порядок сравнения элементов.
# Элементы сравниваются между собой по абсолютной разнице между ними и заданным значением.
# То есть меньшим будет тот, у которого эта разница меньше.


# Задача 20.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# Пример:
# ноутбук
# 12

import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
points_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
text = input().upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))