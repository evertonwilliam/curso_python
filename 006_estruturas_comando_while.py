'''
PROGRAMA: ESTRUTURAS COM PYTHON -  COMANDO WHILE
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
    O while, é um comando de looping. 
    É usado quando não sabemos exatamente quantas vezes o loop deve rodar, 
    Ele irá executar o lado até que a condição seja verdadeira.

OPERADORES
( == ) igual - verifica se algo é igual a outro algo
( != ) diferente - Verifica se algo é diferente de outro algo
( < ) menor - Verifica se algo é menor que outro algo
( > ) maior - Verifica se algo é maior que outro algo
( <= ) menor ou igual - verifica se algo é menor ou igual a outro algo
'''
#declaração da variável contador
int_contador        = 0

# Laço de looping com o comando while
# utilizando o operador menor (<)
while int_contador < 10:
    print("passei aqui por: ", int_contador, "vezes")
    int_contador += 1   # acrescenta 1 na variável, para que ele faça a contagem

print("----------------------------------------------")

# reiniciando a variável.
int_contador = 0 

# Laço de looping com o comando while
# utilizando o operador menor (<=)
while int_contador <= 10:
    print("passei aqui por: ", int_contador, "vezes")
    int_contador += 1   # acrescenta 1 na variável, para que ele faça a contagem