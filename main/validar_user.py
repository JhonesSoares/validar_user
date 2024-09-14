
def fazer_cadastro():
    return f'ooooooooooooooooooooooooo'

def validar_acesso(entrada):
    if entrada in 's':
        print('Faça login:')
        input_user = input('LOGIN: ')
        input_password = input('SENHA: ')

        user_db = 'jhones'
        password_db = '123'

        if input_user == user_db and input_password == password_db:
            return f'Acesso confirmado!'
        return f'Acesso negado!'
    
    if entrada in 'n': return fazer_cadastro()















def main():
    entrada = input('Possui cadastro? sim[s] não[n]: ')

    return validar_acesso(entrada)


print(main())

