'''
PROGRAMA: DICIONÁRIOS EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: APRENDER SOBRE DICIONÁRIOS COM PYTHON

COMANDOS:

'''
import os

# Definindo as variáveis
pessoa      = {}            # dicionário de pessoa
pessoas     = []            # lista de dicionários de pessoas
opcao       = 0             # opção do menu de escolhas
execucao    = True          # faz com que o sistema contine executando


while execucao:
    os.system('cls')    # limpando a tela.

    print("#" * 24)
    print('**** MENU DE OPÇÕES ****')
    print("#" * 24)
    print("# 1. CADASTRO")
    print("# 2. ALTERAÇÃO")
    print("# 3. EXCLUIR")
    print("# 4. LISTAR")
    print('# 5. SAIR')
    print("#" * 24)

    opcao = int(input("Digite a opção desejada: "))         # Temos um bug a ser resolvido aqui. Resolva em seu código.

    if opcao == 1:
        os.system('cls')    # limpando a tela.
        print("******** Cadastrar *********")
        pessoa['nome'] = input("Primeiro Nome: ")
        pessoa['segundo_nome'] = input("Segundo Nome: ")
        pessoa['sobrenome'] = input("sobrenome: ")
        pessoa['idade'] = input("idade: ")
        pessoas.append(pessoa.copy())                  # adiciona os dados para dentro da lista pessoa
        pessoa.clear()

    elif opcao == 2:
        os.system('cls')    # limpando a tela.
        print("******** Alterar *********")        
        nome = input("Digite o nome que será alterado: ")

        for p in pessoas:
            if p["nome"] == nome:
                print("Primeiro Nome: ", p['nome'])
                print("Segundo Nome: ", p['segundo_nome'])
                print("Sobrenome: ", p['sobrenome'])
                print("Idade: ", p['idade'])
                print("=" * 10)

        os.system("pause")  # Agora está fora do loop
        
    elif opcao == 3:
        print("Excluir")

    elif opcao == 4:
        os.system('cls')    # limpando a tela.
        print("***** Listar *******")
        for p in pessoas:
            print("Primeiro Nome: ", p['nome'])
            print("Segundo Nome: ", p['segundo_nome'])
            print("Sobrenome: ", p['sobrenome'])
            print("Idade: ", p['idade'])
            print("=" * 10)
        os.system("pause")
        
    elif opcao == 5:        
        os.system('cls')
        print("encerrando...")
        execucao = False

    else:
        print("Opção não encontrada")