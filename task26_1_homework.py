# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, 
# к нему добавляется количество повторений.

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    
    if not data: return 'None' 
    
    for char in data: 
        # Если предыдущий и текущий символы не совпадают
        if char != prev_char: 
            # затем добавьте количество и символ в нашу кодировку
            if prev_char: 
                encoding += prev_char + str(count)
            count = 1 
            prev_char = char 
        else: 
            # Или увеличить наш счетчик, если символы совпадают
            count += 1 
    else:
        # завершить кодировку
        encoding +=  prev_char + str(count)
        return encoding

encoded_val = rle_encode('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB') 
print(encoded_val)


