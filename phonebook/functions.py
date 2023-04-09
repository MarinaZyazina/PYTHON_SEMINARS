def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio} | {tel_number}')
    print('Успешно!')


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print('Результаты поиска:')
    print(search(tel_book, data))


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def change_data() -> None:
    '''Осуществляет замену элемента в справочнике'''
    data = input('Введите данные для поиска с целью замены: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    tb = tel_book.split('\n')
    print('Результаты поиска с целью замены:')
    b = search(tel_book, data)
    print(b)
    tb[tb.index(b)] = edited(b)
    result = '\n'.join(tb)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write(f'{result}')

def edited(text: str) -> str:
    fio = input()
    tel_number = input()
    if len(fio) == 0:
        fio = text.split(' | ')[0]
    if len(tel_number) == 0:
        tel_number = text.split(' | ')[1]
    return f'{fio} | {tel_number}'


def delete_data() -> None:
    '''Осуществляет удаление записи в справочнике'''
    drop = input('Поиск контакта для удаления: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    result = search(tel_book, drop)
    print(result)
    
    tel_book = tel_book.split('\n') 
    tel_book.remove(result)
    with open('book.txt', 'w', encoding='utf-8') as f:
        for item in tel_book:
            f.write(f'\n{item}')