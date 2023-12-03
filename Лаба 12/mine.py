import json

def load_data(file_name):
    # Функція для завантаження даних з файлу JSON
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Якщо файл не знайдено, повертаємо порожній список
        data = []
    return data

def save_data(file_name, data):
    # Функція для збереження даних у файл JSON
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

def display_data(file_name):
    # Функція для виведення даних на екран
    data = load_data(file_name)
    print(json.dumps(data, indent=2))

def add_record(file_name, record):
    # Функція для додавання нового запису у файл JSON
    data = load_data(file_name)
    data.append(record)
    save_data(file_name, data)

def delete_record(file_name, index):
    # Функція для видалення запису за індексом
    data = load_data(file_name)
    if 0 <= index < len(data):
        del data[index]
        save_data(file_name, data)
        print("Record deleted successfully.")
    else:
        print("Invalid index.")

def search_by_field(file_name, field, value):
    # Функція для пошуку записів за певним полем та значенням
    data = load_data(file_name)
    results = [record for record in data if record.get(field) == value]
    print(json.dumps(results, indent=2))

def calculate_total_cost(file_name):
    # Функція для розрахунку загальної вартості деталей за тиждень
    data = load_data(file_name)
    total_cost = sum(record.get('quantity', 0) * record.get('price', 0) for record in data)
    print(f"Total cost for the week: {total_cost}")

def main():
    data_file = "production_data.json"

    while True:
        print("\nMenu:")
        print("1. Display data")
        print("2. Add record")
        print("3. Delete record")
        print("4. Search by field")
        print("5. Calculate total cost for the week")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice == "1":
            display_data(data_file)
        elif choice == "2":
            # Додавання нового запису
            new_record = {
                'type': input("Enter the type of detail: "),
                'quantity': int(input("Enter the quantity produced per day: ")),
                'price': float(input("Enter the price per detail: "))
            }
            add_record(data_file, new_record)
            print("Record added successfully.")
        elif choice == "3":
            # Видалення запису
            index = int(input("Enter the index of the record to delete: "))
            delete_record(data_file, index)
        elif choice == "4":
            # Пошук за полем та значенням
            field = input("Enter the field to search by: ")
            value = input(f"Enter the {field} value to search for: ")
            search_by_field(data_file, field, value)
        elif choice == "5":
            # Розрахунок загальної вартості
            calculate_total_cost(data_file)
        else:
            print("Invalid choice. Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()
