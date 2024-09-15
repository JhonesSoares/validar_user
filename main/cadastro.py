import json

def fazer_cadastro():
    dados = []
    print('Faça seu cadastro.')

    while True:
        user = str(input('Login: '))
        password = str(input('Senha: '))
        texto = str(input('CADASTRADO! Deseja fazer outro cadastro? sim[s] não[n]: '))

        class PESSOA:
            def __init__(self, user, password) -> None:
                self.user = user
                self.password = password
                
        p1 = PESSOA(user, password)
        
        dados.append(p1.__dict__)
        
        if texto in 'n':
            break

    CAMINHO = 'main\\dados.json'

    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)    

def dados_db(user, paswaord):
    CAMINHO = 'main\\dados.json'
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
            return print(f'Acesso confirmado!')
        return print(f'Acesso negado!')
        
def main():
    fazer_cadastro()
    entrada = input('Deseja fazer login? sim[s] não[n]: ')
    validar_acesso(entrada)


if __name__ == '__main__':
    main()
