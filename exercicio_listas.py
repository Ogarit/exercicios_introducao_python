num = []
for i in range(0, 10):
    n = float(input('Insira um número: ').replace(',', '.'))
    num.append(n)

soma = 0
for i in num:
    soma += i

print(f'A soma destes números é {soma}')
