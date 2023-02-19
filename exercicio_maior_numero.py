n1 = float(input('Digite o 1º número: ').replace(',', '.'))
n2 = float(input('Digite o 2º número: ').replace(',', '.'))
n3 = float(input('Digite o 3º número: ').replace(',', '.'))

if n2 < n1 > n3:
    print(f'O maior número é o {n1}.')
elif n1 < n2 > n3:
    print(f'O maior número é o {n2}.')
else:
    print(f'O maior número é o {n3}.')
