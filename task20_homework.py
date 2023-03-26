# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# Пример:
# ноутбук
# 12

# import re
# def isCyrillic(text):
# 	return bool(re.search('[а-яА-Я]', text))
# points_en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
# points_ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
# text = input().upper()
# if isCyrillic(text):
# 	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
# else:
# 	print(sum([k for i in text for k, v in points_en.items() if i in v]))

# # Оптимальный код (рассмотрен на семинаре 4):
# scrabble = {'б': 3, 'к': 2, 'н': 1, 'о': 1, 'у': 2, 'т': 1} 
# # набираем словарь полностью (это для примера "ноутбук")
# some_word = input()
# summa = 0
# for letter in some_word:
# 	summa += scrabble[letter]
# print(summa)

# ЕЩЕ ВАРИАНТ:

input_str = input("Пожалуйста, ведите слово / Please input the word: ").upper()

scrabble_dict = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1,
				'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3,
				'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

count = 0
for i in range(len(input_str)):
	count = count + scrabble_dict[input_str[i]]
print(count)