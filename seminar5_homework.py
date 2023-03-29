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
        if char != prev_char: 
            if prev_char: 
                encoding += prev_char + str(count)
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else:
        encoding +=  prev_char + str(count)
        return encoding

encoded_val = rle_encode('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB') 
print(encoded_val)

# Cгруппировать слова по общим буквам.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

def group_letter(input_list):
    word_dict = {}
    for word in input_list:
        if (frozenset(word), len(word)) not in word_dict:
            word_dict[(frozenset(word), len(word))] = [word]
        else:
            word_dict[(frozenset(word), len(word))].append(word)
    res_list = []
    for value in word_dict.values():
        res_list.append(value)
    return res_list

print(group_letter(["eat", "tea", "tan", "ate", "nat", "bat"]))