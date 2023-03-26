# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# Input: 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# Output: 6 12

n=(int(input("Введите количество элементов 1-го множества: ")))
num_list_1=[]
for i in range(n):
    num = int(input("Введите элемент 1-го множества: "))
    num_list_1.append(num)
print(num_list_1)

m=(int(input("Введите количество элементов 2-го множества: ")))
num_list_2 = []
for i in range(m):
    num = int(input("Введите элемент 2-го множества: "))
    num_list_2.append(num)
print(num_list_2)

num_list_3 = num_list_1 + num_list_2
print(num_list_3)
num_set = set(num_list_3)
print(num_set)
num_list_total = list(num_set)
num_list_total.sort()
print(num_list_total)