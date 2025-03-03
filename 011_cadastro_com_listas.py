'''
PROGRAMA: PRATICANDO AS FUNCIONALIDADES DA LISTA
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
ENSINAR COMO UTILIZAR A LISTA NO DIA A DIA
'''
import os

# DECLARANDO AS VARIÁVEIS
pessoas         = []    # contém a lista de verduras a serem cadastradas
continua        = True
resposta        = "s"

os.system("cls")
while continua:
    os.system("cls")
    pessoas.append(input("Digite o nome de uma pessoa: ").upper())
    resposta = input("deseja continuar cadastrando? (s ou n) - padrão s: ") or resposta
    # verifica qual é a resposta do usuário
    if resposta != "s":
        continua = False

# Limpa a tela do computador
os.system("cls")

# Inicia o menu de opções
continua = True
while continua:
    print("******************************")
    print("Escolha uma opçao")
    print("1 = Ordenar lista")
    print("2 = Adicionar item na lista")
    print("3 = Remover item da lista")
    print("4 = Sair do Programa")
    print("******************************")

    resposta = input("digite uma das opções acima: ")

    if resposta == "1":
        pessoas.sort()
    elif resposta == "2":
        pessoas.append(input("Digite o nome de uma pessoa: ").upper())
    elif resposta == "3":
        pessoas.remove(input("Digite o nome de uma pessoa: ").upper())
    else:
        continua = False
        os.system("cls")
        print("Programa encerrado")

    if continua:
        for pessoa in pessoas:
            print(pessoa)
        os.system("pause")
        os.system("cls")