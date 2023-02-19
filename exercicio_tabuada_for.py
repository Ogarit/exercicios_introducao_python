n = float(input('Digite um número: ').replace(',', '.'))

print('-' * 20)

for i in range(0, 11):
    print(f'{n} * {i} = {n * i}')

print('-' * 20)
