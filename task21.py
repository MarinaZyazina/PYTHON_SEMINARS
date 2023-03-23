# Напишите программу для печати всех уникальных значений в словаре.
# Пример:
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, 
# {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Словарь вводит пользователь.

input_dict = {}
input_dict_len = int(input("Введите количество пар: "))
for _ in range(input_dict_len): 
    input_key = input("Введите ключ: ") 
    input_value = input("Введите значение: ")
    input_dict[input_key] = input_value
    
print(set(input_dict.values()))