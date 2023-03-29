# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def max_replace_min(input_list: list):
    min_number = input_list[0]
    max_number = input_list[0]
    for i in range(len(input_list)):
        if input_list[i] > max_number:
            max_number = input_list[i]
        if input_list[i] < min_number:
            min_number = input_list[i]
    for i in range(len(input_list)):
        if input_list[i] == max_number:
            input_list[i] = min_number
        
input_list = []
list_len = int(input("Введите количество элементов в списке: "))
for _ in range(list_len):
    input_list.append(int(input(f"Введите число: ")))
print(input_list)
    
max_replace_min(input_list)
print(input_list)