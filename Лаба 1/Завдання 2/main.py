long = 10 # пройшов 10 км
days = 1 # за пешрий день пройшов 10км
progress = 0 #прогрес спортсмена в подоланні дистанції, на 10% більше, ніж попереднього дня
while long < 50:
    progress = long * 0.1
    long = long + progress
    days = days + 1
print(days)
