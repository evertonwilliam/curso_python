'''
PROGRAMA: ESTRUTURAS COM PYTHON -  COMANDO IF
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
    O comando if é usado para tomar decisões no código. 
    Se a condição for verdadeira, um bloco de código é executado. 
    O else define o que acontece caso a condição seja falsa. 
    Já o elif (else if) permite testar várias condições diferentes antes de chegar ao else.

OPERADORES
( == ) igual - verifica se algo é igual a outro algo
( != ) diferente - Verifica se algo é diferente de outro algo
( < ) menor - Verifica se algo é menor que outro algo
( > ) maior - Verifica se algo é maior que outro algo
( <= ) menor ou igual - verifica se algo é menor ou igual a outro algo
'''

# Declaração de variáveis globais
str_usuario     = ""
str_senha       = ""

# Declaração de constantes
USUARIO         = "maria@maria.com.br"
SENHA           = "123456"

# Solicitando as informações para o usuário
str_usuario     = input("Digite o seu usuário: ")
str_senha       = input("Digite a sua senha: ")


# Efetuando a verificação de apenas 1 dos valores.
if str_usuario == USUARIO:
    print("Usuário está correto")
else:
    print("Usuário está errado")

# Efetuando a verificação dos dois valores, um ou outro verdadeiro
if str_usuario == USUARIO or str_senha == SENHA:
    print("O usuário ou a senha estão corretos: ", str_usuario, str_senha)
else:
    print("O usuário e a senha estão incorretos: ", str_usuario, str_senha)

# Efetuando a verificação dos dois valores, um e outro ambos devem ser verdadeiros
if str_usuario == USUARIO and str_senha == SENHA:
    print("O usuário e a senha estão corretos: ", str_usuario, str_senha)
else:
    print("O usuário ou a senha estão incorretos: ", str_usuario, str_senha)

# Efetuando a verificação serial do usuário e da senha:
if str_usuario != USUARIO:
    print("O usuário está errado, tente novamente: ", str_usuario)
elif str_senha != SENHA:
    print("A senha está incorreta, tente novamente: ", str_senha)
elif str_usuario == USUARIO and str_senha == SENHA:
    print("Login executado com sucesso, seja bem vindo(a): ", str_usuario)

# utilizando o operador not in com lista pré definida.
str_operador    = input("Digite o operador matemático (+) (-) (/) (*): ")
print(str_operador)
if  str_operador not in ["+", "-", "/", "*"]:
    print("O operador matemático não é válido digite: + ou - ou * ou /")
    error = True
else:
    error = False
