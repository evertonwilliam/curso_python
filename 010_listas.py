'''
PROGRAMA: APRENDENDO SOBRE LISTAS
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
    Listas são coleções ordenadas, portanto você pode acessar qualquer
    elemento de uma lista informando a posição – ou índice – do item
    desejado ao interpretador Python.
'''
# CRIANDO A LISTA
carros = ["Ford", "Chevrolet", "Fiat", "Hiuday"]

# MOSTRANDO O VALOR TOTAL DA LISTA
print ("Aqui estão todos os carros",carros)

# ACESSANDO ITEM A ITEM DA LISTA
print("Carro 0 da lista: ", carros[0])
print("Carro 1 da lista: ", carros[1])
print("Carro 2 da lista: ", carros[2])

# CRIANDO UMA LISTA DE FORMA DINÂMICA
legumes = []
print("A lista está vazia?: ", legumes)

# ADICIONANDO DADOS NA LISTA
legumes.append("chuchu")
legumes.append("pepino")

# MOSTRANDO O CONTEÚDO DA LISTA
print("A lista está vazia?: ", legumes)
print("Mostrando 1 item da lista", legumes[0])

# ALTERANDO O VALOR DE UM ITEM DA LISTA
legumes[0] = "repolho"
print("A lista teve o seu valor alterado", legumes)

# REMOVENDO UM ITEM DA LISTA
del legumes[0]
print("A lista teve o seu item removido", legumes)

print("********************* TREINANDO *************************")

verduras = []
verduras.append("Cebolinha")
verduras.append("Salsinha")
verduras.append("Alface")
verduras.append("Agrião")
verduras.append("Rucula")
verduras.append("Couve")
verduras.append("Couve-flor")
verduras.append("Escarola")
verduras.append("Agrião")

print("*** O Agrião aparece", verduras.count("Agrião"), "vezes na lista")
print("*** A lista tem:", len(verduras), "informações")

#verduras.sort()     # Ordena a lista
#verduras.reverse()  # Inverte a ordem da lista


# listando as informações separadamente
for verdura in verduras:
    print(verdura)


# Removendo item na lista e vendo qual foi removido
removido = verduras.pop(0)
print("O item removido com POP foi", removido)
print("A nova lista é: ", verduras)

