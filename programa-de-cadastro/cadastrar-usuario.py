usuarios = []

def cadastrar_usuario():
    cadastro_usuario = {}
    cadastro_usuario['nome'] = input('Nome: ').title()
    cadastro_usuario['idade'] = int(input('Idade: '))
    cadastro_usuario['email'] = input('Email: ')
    return cadastro_usuario

def mostrar_usuarios():
    if not usuarios:
        print('Nenhum usuário cadastrado!')
    else:
        print(f"{' USUÁRIOS CADASTRADOS ':-^40}")
        for i, p in enumerate(usuarios, 1):
            print(f"{i}. Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")

while True:
    cadastro = input('Cadastrar novo usuário? (S/N): ').upper()
    if cadastro == 'N':
        mostrar_usuarios()
        break
    elif cadastro == 'S':
        usuarios.append(cadastrar_usuario())
    else:
        print('Opção inválida! Digite S ou N.')




    
