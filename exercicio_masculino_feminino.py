sexo = input('Digite o sexo da pessoa[M: Masculino, F: Feminino]: ')

if sexo.upper() in ['M', 'MASCULINO', 'HOMEM']:
    print('O sexo é masculino.')
elif sexo.upper() in ['F', 'FEMININO', 'MULHER']:
    print('O sexo é feminino.')
else:
    print('Inválido!')
