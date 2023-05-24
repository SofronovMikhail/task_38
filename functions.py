def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    print(data)
    data_to_find = input('Введите данные для поиска: ')
    print(search(data, data_to_find, 0, 0))
    


def search(book: str, info: str, count: int, result_search: int) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    if count == 1:
        return result_search
    else:
        result_search =list()
        book = book.split('\n')
        for contact in book:
            if info in contact:
                result_search.append(contact)
        if len(result_search) == 0:
            return 'Совпадений не найдено'
        if len(result_search) == 1:
            return result_search
        count = len(result_search)
        if len(result_search) > 1:
            result_search = '\n'.join(result_search)
            print(result_search)
            data_to_find = input('Уточните данные для поиска: ')
            book = result_search
            return search(book, data_to_find, count, result_search)
        
def add_changes_data() -> None:
    """Добавляет измененную информацию в справочник."""
    data = input('Введите какой контакт хотите редактировать: ')
    new_contact = changes_data(data)
    with open('book.txt', 'w', encoding='utf-8') as file: 
        file.write(new_contact)


def changes_data(contact: str) -> None:
    """Изменяут информацию в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        all_data = file.read()
    changes_contact = search(all_data, contact, 0, 0)
    print(changes_contact)
    changes_contact = '\n'.join(search(all_data, contact, 0, 0))
    all_data = all_data.split('\n')
    for i in range(len(all_data)):
        if changes_contact == all_data[i]:
            fio = input('Введите ФИО: ')
            phone = input('Введите номер телефона: ')
            all_data[i] = f'{fio} | {phone}'
    all_data = '\n'.join(all_data)
    print(all_data)
    return all_data


def remove_data() -> None:
    """Добавляет  информацию в справочник без удаленного контакта."""
    data = input('Введите какой контакт хотите удалить: ')
    new_contact = remove(data)
    with open('book.txt', 'w', encoding='utf-8') as file: 
        file.write(new_contact)


def remove(contact: str) -> None:
    """Удаляет выбранную информацию в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        all_data = file.read()
    changes_contact = search(all_data, contact, 0, 0)
    print(changes_contact)
    changes_contact = '\n'.join(search(all_data, contact, 0, 0))
    all_data = all_data.split('\n')
    for i in all_data:
        if changes_contact == i:
            all_data.remove(changes_contact)
    all_data = '\n'.join(all_data)
    print(all_data)
    return all_data        


        
   
