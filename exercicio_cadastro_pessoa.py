pessoas = []
while True:
    escolha = int(input('Digite 1 para cadastrar uma pessoa e 2 para parar o programa: '))

    if escolha == 1:
        pessoas.append({
            'nome': input('Digite o nome da pessoa: ').strip(),
            'idade': int(input('Digite a idade da pessoa: ')),
            'altura': float(input('Digite a altura da pessoa: ').replace(',', '.'))
        })
    elif escolha == 2:
        break
    else:
        print('Valor inválido!')

for pessoa in pessoas:
    print(pessoa)
