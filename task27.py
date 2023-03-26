# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

input_str = input("введите текст: ").upper() + " "
count = 1
word_list = set()
word = ""
for char in input_str: 
    if char != " ":
        word += char 
    else: 
        word_list.add(word) 
        word = ""
print(len(word_list))