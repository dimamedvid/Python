def create(name, content):
    try:
        with open(name, 'w') as file:
            file.write(content)
        print(f"Файл {name} створено.")
    except Exception as e:
        print(f"Помилка при створенні файлу {name}: {e}")
def process(input_file, output_file, line_length):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = ''.join(c for c in line if c.isdigit())
                line = line.ljust(line_length)
                outfile.write(line + '\n')
        print(f"Файл {output_file} оброблено.")
    except Exception as e:
        print(f"Помилка при обробці файлів: {e}")
def print_file(name):
    try:
        with open(name, 'r') as file:
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Помилка при читанні файлу {name}: {e}")

# Завдання а: створення файлу TF11_1
create('TF11_1.txt', '123456789\nabcdefghij\nklmnopqrst\n')

# Завдання б: обробка файлу TF11_1 та створення файлу TF11_2
process('TF11_1.txt', 'TF11_2.txt', 10)

# Завдання в: виведення вмісту файлу TF11_2
print_file('TF11_2.txt')
