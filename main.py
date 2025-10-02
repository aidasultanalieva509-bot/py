abiturient = [
    {'name': 'Radomir', 'OPT': 110, 'gender': 'male'},
]

def display_contacts():
    print("\nТекущие контакты:")
    if not abiturient:
        print("Список пуст.")
    else:
        for i, contact in enumerate(abiturient, 1):
            print(f"{i}. Имя: {contact['name']}, Номер: {contact['OPT']}, Пол: {contact['gender']}")

def create_contact():
    name = input("Введите имя нового контакта: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return

    try:
        number = int(input("Введите номер нового контакта: ").strip())
    except ValueError:
        print("Номер должен быть числом.")
        return

    for contact in abiturient:
        if contact['name'].lower() == name.lower():
            print(f"Контакт с именем {name} найден. Обновляем номер.")
            contact['OPT'] = number
            print("Номер обновлен.")
            return

    gender = input("Введите пол (male/female): ").strip().lower()
    if gender not in ('male', 'female'):
        print("Пол задан неверно. Используем значение 'male' по умолчанию.")
        gender = 'male'

    abiturient.append({'name': name, 'OPT': number, 'gender': gender})
    print("Контакт добавлен.")

def edit_contact():
    name = input("Введите имя контакта для редактирования: ").strip()
    for contact in abiturient:
        if contact['name'].lower() == name.lower():
            new_name = input("Введите новое имя: ").strip()
            try:
                new_number = int(input("Введите новый номер: ").strip())
            except ValueError:
                print("Номер должен быть числом.")
                return

            for c in abiturient:
                if c != contact:
                    if c['name'].lower() == new_name.lower():
                        print("Ошибка: такое имя уже существует.")
                        return
                    if c['OPT'] == new_number:
                        print("Ошибка: такой номер уже существует.")
                        return

            contact['name'] = new_name
            contact['OPT'] = new_number
            print("Контакт изменён.")
            return
    print("Контакт не найден.")

def delete_contact():
    name = input("Введите имя контакта для удаления: ").strip()
    for i, contact in enumerate(abiturient):
        if contact['name'].lower() == name.lower():
            del abiturient[i]
            print("Контакт удалён.")
            return
    print("Контакт не найден.")

def main():
    while True:
        display_contacts()
        print("\nВыберите действие:")
        print("1 - Добавить контакт")
        print("2 - Изменить контакт")
        print("3 - Удалить контакт")
        print("4 - Выход")
        choice = input("Введите номер команды: ").strip()

        if choice == '1':
            create_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
