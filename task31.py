# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21 # ? Почему 21? Если с 1, то 8, если с 0, то 13

# Задание необходимо решать через рекурсию

# def fibonachi(serial_number):
#     if serial_number in [1, 2]:
#         return 1
#     return fibonachi(serial_number - 1) + fibonachi(serial_number - 2)
# print(fibonachi(7)) # Вывод: 13

# Цикл:
def fibonachi_iteration(serial_number): 
    first = 0 
    second = 1 
    if serial_number == 1: 
        return first 
    if serial_number == 2: 
        return second 
    count = 1 # count = 2
    while serial_number != count: 
        third = first + second 
        first = second 
        second = third 
        count += 1 
    return third
print(fibonachi_iteration(7)) # Вывод: 13