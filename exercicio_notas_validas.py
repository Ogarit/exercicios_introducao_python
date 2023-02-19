while True:
    n = float(input('Insira a nota do aluno: ').replace(',', '.'))

    if 0 <= n <= 10:
        print(f'A nota do aluno é {n}')
        break
    else:
        print(f'A nota do aluno é inválida!')
