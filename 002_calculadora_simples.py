'''
PROGRAMA: CALCULADORA SIMPLES EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: EFETUAR A SOMA DE DOIS NÚMEROS SOLICITADOS PELO SISTEMA

COMANDOS:
INPUT = SOLICITA UM VALOR PARA O USUÁRIO
PRINT = IMPRIME EM TELA DO QUE FOI CALCULADO
OPERADOR (+)
INT() = CONVERSOR DE TIPO DE OPERADORES
'''

# declaração das variáveis
int_primeiro_numero = 0
int_segundo_numero  = 0
int_resultado       = 0

# solicitando valores ao usuario e guardando nas variáveis
# int() converte o dado para inteiro
int_primeiro_numero = int(input("Digite o primeiro número: ")) 
int_segundo_numero = int(input("Digite o segundo número: "))   

# aplicando o calculo entre as variáveis
int_resultado = int_primeiro_numero + int_segundo_numero

# apresentando o resultado em tela
print("O resultado da soma é: ", int_resultado)