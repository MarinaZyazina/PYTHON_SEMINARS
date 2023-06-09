# Задача семинар 8.
# Создать телефонный справочник с возможностью 
# импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - 
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик 
# для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. 
# Ваша программа не должна быть линейной

# Домашнее задание к семинару. 
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.
# Логика алгоритма для изменения:
# 1. Прочитать в переменную информацию из файла.
# 2. Внести нужные правки в этой информации (для этого 
# можно вызвать поиск, чтобы понять, что конкретно меняем).
# 3. Перезаписать файл через 'w'.
# P.S. Для уточнения поиска редактируемого элемента можно воспользоваться
# функцией enumerate.
# Для нахождения индекса вхождения в массиве можно использовать index (<вхождение>).

import functions

while True:
    print('1. вывод, 2. добавление, 3. поиск, 4. изменить, 5. удалить')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
        functions.change_data()
    elif mode == 5:
        functions.delete_data()
    else:
        break
    


# with open('book.txt', 'w', encoding='utf-8') as f:
#     f.write('фио | номер телефона')

# with open('book.txt', 'a', encoding='utf-8') as f:
#     f.write('\nфио1 | номер телефона1') #\n позволяет записать с новой строки

# with open('book.txt', 'r', encoding='utf-8') as f:
#     print(f.read()) #если исп. эту функцию, то на выходе вся информация из файла