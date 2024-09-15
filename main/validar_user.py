import json
 
def dados_db(user, paswaord):
    CAMINHO = 'main\\dados_pessoas.json'
    with open(CAMINHO, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)

    for i in dados:
        if i['user'] == user and i['password'] == paswaord:
            return True
    return False

def validar_acesso(entrada):
    if entrada in 's':
        print('Faça login:')
        input_user = input('LOGIN: ')
        input_password = input('SENHA: ')

        if dados_db(input_user, input_password):
            return f'Acesso confirmado!'
        return f'Acesso negado!'
    return
    
def main():
    entrada = input('Deseja fazer login? sim[s] não[n]: ')

    return validar_acesso(entrada)


if __name__ == '__main__':
    main()

