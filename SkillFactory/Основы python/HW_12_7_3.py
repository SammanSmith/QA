per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money = int(input('Введите сумму >>> '))

for v in per_cent.values():
    deposit.append(int(money / 100 * v))

print(deposit)
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')
