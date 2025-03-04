'''
PROGRAMA: DICIONÁRIOS EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: APRENDER SOBRE DICIONÁRIOS COM PYTHON

COMANDOS:

'''
# criando um dicionário vazio
d_pessoa_1 = {}

# incluindo dados no dicionário
d_pessoa_1['nome']          = "Maria"
d_pessoa_1['sobrenome']     = "Ferreira"
d_pessoa_1['idade']         = "14"

# Mostrando o conteúdo do dicionário
print(d_pessoa_1)

# adicionando novos itens
d_pessoa_1.update({'Cidade':'Votuporanga'})
d_pessoa_1['UF'] = 'SP'

# mostrando o que foi acrescentado
print(d_pessoa_1)

# apagando um item do dicionário
del(d_pessoa_1['UF'])
print(d_pessoa_1)

# ordenando as chaves de um dicionário
print(dict(sorted(d_pessoa_1.items())))

# mostrando um item de um dicionário
print(d_pessoa_1['nome'].title())

# criando um cadastro de pessoas com dicionários
pessoa_1 = {'nome':'maria', 'sobrenome':'sampaio', 'idade':'14'}
pessoa_2 = {'nome':'carla', 'sobrenome':'teodoro', 'idade':'13'}
pessoa_3 = {'nome':'joana', 'sobrenome':'levinsk', 'idade':'12'}
pessoa_4 = {'nome':'pedro', 'sobrenome':'neves', 'idade':'10'}
pessoa_5 = {'nome':'joão', 'sobrenome':'ambrozio', 'idade':'18'}
pessoa_6 = {'nome':'marcos', 'sobrenome':'oliveira', 'idade':'19'}

pessoas = [pessoa_1, pessoa_2, pessoa_3, pessoa_4, pessoa_5, pessoa_6]

print(pessoas)

# Percorrendo a lista e formatando a saída
for pessoa in pessoas:
    print("Nome: ", pessoa['nome'].title())
    print("Sobrenome: ", pessoa['sobrenome'].title())
    print("Idade: ", pessoa['idade'])
    print("===========") 
