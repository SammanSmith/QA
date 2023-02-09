ticket = int(input("Сколько билетов хотите приобрести? >>> "))

total = 0

for i in range(ticket):
    age = int(input('Введите возраст >>> '))
    if 18 < age < 25:
        total += 990
    elif age > 25:
        total += 1390

if ticket > 3:
    print(total - total * .1)
else:
    print(total)
