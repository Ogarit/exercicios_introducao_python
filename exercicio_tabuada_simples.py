n = float(input('Insira um número: ').replace(',', '.'))

print('-' * 20)

i = 0
while i <= 10:
    print(f'{n} * {i} = {n * i}')

    i += 1

print('-' * 20)
