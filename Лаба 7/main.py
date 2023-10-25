def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: Потужність - {value[0]} к.с., Ціна - {value[1]} грн")

def add_to_dictionary(dictionary, key, power, price):
    dictionary[key] = (power, price)

def remove_from_dictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    else:
        print(f"Ключ '{key}' відсутній у словнику.")

def calculate_total_price(dictionary, threshold):
    total_price = 0
    for key, value in dictionary.items():
        if value[0] > threshold:
            total_price += value[1]
    return total_price

# Створення словника з даними про потужність двигуна і вартість автомобілів
cars = {
    "Car1": (120, 15000),  # Приклад даних для автомобіля 1
    "Car2": (90, 11000),  # Приклад даних для автомобіля 2
    "Car3": (110, 13000),  # Приклад даних для автомобіля 3
    "Car4": (130, 18000),  # Приклад даних для автомобіля 4
    "Car5": (95, 10000),  # Приклад даних для автомобіля 5
    "Car6": (105, 12000),  # Приклад даних для автомобіля 6
    "Car7": (140, 20000),  # Приклад даних для автомобіля 7
    "Car8": (70, 8000),  # Приклад даних для автомобіля 8
    "Car9": (115, 16000),  # Приклад даних для автомобіля 9
    "Car10": (125, 17000)  # Приклад даних для автомобіля 10
}
while True:
    print("\nОберіть операцію:")
    print("1. Вивести всі значення словника")
    print("2. Додати новий запис до словника")
    print("3. Видалити запис зі словника")
    print("4. Порахувати загальну ціну автомобілів з потужністю більше 100 к.с.")
    print("5. Вийти з програми")

    choice = input("Ваш вибір: ")

    if choice == '1':
        print_dictionary(cars)
    elif choice == '2':
        key = input("Введіть ключ: ")
        power = int(input("Введіть потужність (к.с.): "))
        price = int(input("Введіть ціну (грн): "))
        add_to_dictionary(cars, key, power, price)
    elif choice == '3':
        key = input("Введіть ключ для видалення: ")
        remove_from_dictionary(cars, key)
    elif choice == '4':
        threshold = 100
        total_price_threshold = calculate_total_price(cars, threshold)
        print(f"Загальна ціна автомобілів з потужністю більше {threshold} к.с.: {total_price_threshold} грн")
    elif choice == '5':
        break
    else:
        print("Невірний вибір операції. Спробуйте ще раз.")
