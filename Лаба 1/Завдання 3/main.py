n = int(input("Введіть число n: "))

for i in range(n, 0, -1):
    for k in range(n - 1):
        print(" ", end=" ")
    for j in range(i, n + 1):
        print(j, end=" ")
    print()

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()