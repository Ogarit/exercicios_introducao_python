n = float(input('Insira um número: ').replace(',', '.'))

if n > 0:
    print(f'O número {n} é positivo')
elif n < 0:
    print(f'O número {n} é negativo')
else:
    print('0 é um número nulo')
