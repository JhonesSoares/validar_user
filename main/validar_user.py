import json

def fazer_cadastro():
    dados = []
    print()
    print('Faça seu cadastro.')

    while True:
        nome = str(input('Nome: '))
        senha = str(input('Senha: '))
        texto = str(input('CADASTRO REALIZADO! Deseja fazer outro cadastro? sim[s] não[n]: '))
        print()

        class PESSOA:
            def __init__(self, nome, senha) -> None:
                self.nome = nome
                self.senha = senha
                
        p1 = PESSOA(nome, senha)
        
        dados.append(p1.__dict__)
        
        if texto in 'n':
            break

    CAMINHO = 'main\\dados_pessoas.json'

    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)    

    with open(CAMINHO, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
    
    return dados

def validar_acesso(entrada):
    if entrada in 's':
        print('Faça login:')
        input_user = input('LOGIN: ')
        input_password = input('SENHA: ')

        user_db = fazer_cadastro()[0]['nome']
        password_db = fazer_cadastro()[1]['senha']

        if input_user == user_db and input_password == password_db:
            return f'Acesso confirmado!'
        return f'Acesso negado!'
    
    if entrada in 'n': return fazer_cadastro()















def main():
    entrada = input('Possui cadastro? sim[s] não[n]: ')

    return validar_acesso(entrada)


print(main())

