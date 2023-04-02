# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, 
# к нему добавляется количество повторений.

# # Вариант 1
# def rle_encode(data): 
#     encoding = '' 
#     prev_char = '' 
#     count = 1 
    
#     if not data: return 'None' 
    
#     for char in data: 
#         # Если предыдущий и текущий символы не совпадают
#         if char != prev_char: 
#             # затем добавьте количество и символ в нашу кодировку
#             if prev_char: 
#                 encoding += prev_char + str(count)
#             count = 1 
#             prev_char = char 
#         else: 
#             # Или увеличить наш счетчик, если символы совпадают
#             count += 1 
#     else:
#         # завершить кодировку
#         encoding +=  prev_char + str(count)
#         return encoding

# encoded_val = rle_encode('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB') 
# print(encoded_val) # A4B3C2X1Y1Z1D4E3F3A6B28. А должен быть A4B3C2XYZD4E3F3A6B28

# Вариант 2 (разбор на семинаре 6)

def rle(some_str):
    res_list = []
    some_str += ' '
    temp_letter = some_str[0]
    count_letter = 1
    for ind in range(1, len(some_str)):
        if some_str[ind] == temp_letter:
            count_letter += 1
        else: 
            if count_letter == 1:
                res_list.append(f'{temp_letter}')
            else:
                res_list.append(f'{temp_letter}{count_letter}')
            count_letter = 1
            temp_letter = some_str[ind]
    print(res_list) # Вывод: ['A4', 'B3', 'C2', 'X', 'Y', 'Z', 'D4', 'E3', 'F3', 'A6', 'B28']
    print(*res_list, sep='') # Вывод: A4B3C2XYZD4E3F3A6B28 

rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB')

