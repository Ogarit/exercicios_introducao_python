usuario = 'tiago'
senha = '1234'

while True:
    usuario_login = input('Digite o usúario: ')
    senha_login = input('Digite a senha: ')

    if usuario_login == usuario and senha_login == senha:
        print('Login realizado!')
        break
    else:
        print('Usúario ou senha inválido!')
