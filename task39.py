# Даны два массива чисел. 
# Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), 
# которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

def cross_arrays(input_arr_1, input_arr_2):
    second_set = set(input_arr_2) # множество из второго массива
    result = []
    for i in input_arr_1:
        if i not in second_set:
            result.append(i)
    return result

len_first_array = int(input("Введите длинну первого масива: "))
first_array = []
for i in range(len_first_array):
    first_array.append(input(f"Введите {i + 1}-й элемент первого массива: "))

len_second_array = int(input("Введите длинну второго масива: "))
second_array = []
for i in range(len_second_array):
    second_array.append(input(f"Введите {i + 1}-й элемент второго массива: "))
print(cross_arrays(first_array, second_array))