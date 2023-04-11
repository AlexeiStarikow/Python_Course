# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
import csv

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def show_menu2():
    print("Выберите необходимое действие:\n"
          "1.Удалить запись\n "
          "2.Изменить фамилию\n"
          "3.Изменить имя\n"
          "4.Изменить номер телефона\n"
          "5.Изменить описание\n"
          "6.Выйти в главное меню")
    choice = int(input())
    return choice


def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding = 'utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def print_result(data: list):
    for el in data:
        for k, v in el.items():
            print(f'{k}: {v}')
        print()
    input("Для продолжения нажмите Enter")


def fine_abonent_lastname(data):
    lastname = input("Введите фамилию абонента: ")
    count = 0
    index = 0
    found_abonent = []
    for el in data:
        if lastname in el['Фамилия']:
            count += 1
            found_abonent.append(el)
            print(count, "найденный абонент")
            for k, v in el.items():
                print(f'{k}: {v}')
            print()
    if count > 1:
        index = int(input("Найдено несколько абонентов\n"
                          "Чтобы вернуться назад нажмите 0\n"
                          "Чтобы изменить контакт, введите его номер: "))
        if index > 0:
            count = 1
            index -= 1
            print()
    if count == 1:
        choise = 0
        while choise != 6:
            choise = show_menu2()
            if choise == 1:
                data.remove(found_abonent[index])
                print("Абонент удален\n")
            if choise == 2:
                found_abonent[index]['Фамилия'] = input(
                    "Введите новую фамилию: ")
                print("Изменения приняты\n")
            if choise == 3:
                found_abonent[index]['Имя'] = input("Введите новон имя: ")
                print("Изменения приняты\n")
            if choise == 4:
                found_abonent[index]['Телефон'] = input(
                    "Введите новый телефон: ")
                print("Изменения приняты\n")
            if choise == 5:
                found_abonent[index]["Описание"] = input(
                    "Введите новое описание: ")
                print("Изменения приняты\n")
    if count == 0:
        print("Фамилия не найдена")
        print()
        input("Для продолжения нажмите клавишу Enter")


def find_abobent_number(data):
    number = input("Введите номер абонента: ")
    count = 0
    for el in data:
        if el['Телефон'] == number:
            count += 1
            for k, v in el.items():
                print(f'{k}: {v}')
            print()
    if count == 0:
        print("Номер не найден")
        print()
    input("Для продолжения нажмите клавишу Enter")


def add_abonent(data):
    list1 = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    list1.append(input("Введите фамилию: "))
    list1.append(input("Введите имя: "))
    list1.append(input("Введите телефон: "))
    list1.append(input("Введите описание: "))
    new_abonent = dict(zip(fields, list1))
    data.append(new_abonent)
    print()
    print("Новая запись добавлена")
    input("Для продолжения нажмите Enter")


def save_phonebook(data):
    with open(input("Введите имя файла: "), 'w', encoding='utf-8') as new_file:
        for i in data:
            str_i = ''
            for v in i.values():
                str_i += v + ','
            str_i = str_i[:-1]
            new_file.write(str_i + '\n')
    print("Справочник сохранен")
    input("Для продолжения нажмите Enter")
    

phonebook = read_csv("phonebook.csv")
choice = 0
while choice != 6:
    choice = show_menu()
    if choice == 1:
        print_result(phonebook)
    if choice == 2:
        fine_abonent_lastname(phonebook)
    if choice == 3:
        find_abobent_number(phonebook)
    if choice == 4:
        add_abonent(phonebook)
    if choice == 5:
        save_phonebook(phonebook)
 