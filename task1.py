money = float(input("Введите сумму, которую человек планирует положить под проценты:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
for key in per_cent:
    deposit.append(money * per_cent[key] / 100)
print(deposit)
i=max(deposit)
print(i)
