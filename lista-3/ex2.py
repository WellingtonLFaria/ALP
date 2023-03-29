username = ''
password = ''

print('Cadastro de usuário')
while username == password:
    try:
        username = str(input('Nome de Usuário: '))
    except ValueError:
        print('Por favor informe um Nome de Usuário válido!')
    
    try:
        password = str(input('Senha: '))
        if password == username:
            print(f'Não é possível utilizar os mesmos valores para Senha e Nome de Usuário\nTente Novamente!')
    except:
        print('Por favor insira uma Senha válida!')
    