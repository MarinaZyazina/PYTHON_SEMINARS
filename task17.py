# Дан список чисел. Определите, 
# сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

input_list = []
list_len = int(input('Введите количество элементов в списке: '))
for _ in range(list_len):
    input_list.append(int(input('Введите число: ')))
print(input_list)

input_set = set(input_list)
print(f'Различных чисел {len(input_set)}')