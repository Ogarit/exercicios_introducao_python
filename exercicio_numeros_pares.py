n = int(input('Insira um número: '))

print(f'Estes são os números pares de 0 a {n}')

i = 1
while i <= n:
    if i % 2 == 0:
        print(f'{i}')

    i += 1
