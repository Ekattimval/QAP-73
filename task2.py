n = int(input("Введите количество билетов:"))
age = int(input("Введите возраст посетителя:"))
s = 0
for i in range(n):
    if age < 18:
        s += 0
    elif 18 <= age <25:
        s += 990
    else:
        s += 1390
if n > 3:
    count = 0.9
else:
    count = 1
    print("Сумма со скидкой", s*count)