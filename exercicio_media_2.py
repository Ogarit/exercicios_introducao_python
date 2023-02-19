nota1 = float(input('Insira a 1ª nota: ').replace(',', '.'))
nota2 = float(input('Insira a 2ª nota: ').replace(',', '.'))
nota3 = float(input('Insira a 3ª nota: ').replace(',', '.'))
nota4 = float(input('Insira a 4ª nota: ').replace(',', '.'))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(f'O aluno foi aprovado com a nota {media}.')
elif media >= 4:
    print(f'O aluno está de recuperação com a nota {media}.')
else:
    print(f'O aluno está reprovado com a nota {media}.')
