import json

def fazer_cadastro():
    dados = []
    print()
    print('Crie seu login.')

    while True:
        user = str(input('Nome: '))
        password = str(input('Senha: '))
        texto = str(input('LOGIN CADASTRADO! Deseja fazer outro cadastro? sim[s] não[n]: '))
        print()

        class PESSOA:
            def __init__(self, user, password) -> None:
                self.user = user
                self.password = password
                
        p1 = PESSOA(user, password)
        
        dados.append(p1.__dict__)
        
        if texto in 'n':
            break

    CAMINHO = 'main\\dados_pessoas.json'

    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)    


if __name__ == '__main__':
    fazer_cadastro()
