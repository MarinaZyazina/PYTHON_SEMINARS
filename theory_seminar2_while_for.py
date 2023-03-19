# ТЕОРИЯ
# Цикл While:
# Вводятся числа, пока не введется 0. Найти сумму чисел, кратных 3.
# summa = 0
# while True:
#     number = int(input())
#     if number ==0:
#         break
#     elif number % 3 == 0:
#         summa += number
# print(summa)

# Сумма цифр числа:
# number = int(input()) #56783
# summa = 0
# while number > 0:
#     summa += number % 10
#     number //= 10
# print(summa)

# Цикл For:
# for letter in 'привет': #строка
#     print(letter)

# числовая последовательность:
# for i in 1, 4, 2, 5, 9, 10:
#     print(i)

# функция range:
# for i in range(10): 
# #три аргумента: левая и правая граница, шаг. Здесь по умолчанию левая граница 0, шаг 1.
#     print(i)

# for i in range(5, 10, 2): # от 5 до 10 с шагом 2. Вывод: 5 7 9
#     print(i)

# for i in range(10, 4, -1): # В обратную сторону. Вывод: 10 9 8 7 6 5
#     print(i)

# переменная-итератор используется:
# for i in range(1, 11):
#     print(i ** 2) # возведение в квадрат

# переменная-итератор не используется:
# for i in range(5):
#     print('hello') # Вывод hello 5 раз

# ИЛИ i заменяют на _
# for _ in range(5):
#     print('hello') # Вывод hello 5 раз

a = 'hello'
for i in range(0, len(a), 2): #Вывод: h l o (с индексом 0, 2, 4)
    print(a[i])


