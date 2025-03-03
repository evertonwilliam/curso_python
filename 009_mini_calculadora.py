'''
PROGRAMA: DESENVOLVENDO UMA MINI CALCULADORA COM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
    Após aprender os recursos básicos da linguagem Python, você está apto a desenvolver um
    aplicação mínima sem necessidade de aprender outros recursos. A calculadora irá mostrar
    como é simples utilizar o python para desenvolver soluções com pouco conhecimento.

    PARA ESTE PROJETO, VAMOS UTILIZAR A METODOLOGIA DE ENSINO, CONSIDERANDO:
        DECLARAÇÕES DE VARIÁVEIS GLOBAIS COM INDICADOR DE TIPO
        SOLICITAÇÃO DE DADOS PARA O USUÁRIO

ATENÇÃO:
    SIM, EXISTE FORMAS DIFERENTES PARA EXECUTAR ESTA CALCULADORA, MAS A GENTE VAI APRENDENDO POUCO A POUCO.        

'''
# DECLARAÇÃO DE VARIÁVEIS GLOBAIS
f_numero_a      = 0.00       # declaração de variável float a
f_numero_b      = 0.00       # declaração da variável float b
str_operador    = ""         # declaração da variável string do operador matemático
error           = True       # validação dos erros no try
resultado       = 0.0        # declaração da veriável resultado

# SOLICITANDO OS DADOS PARA O USUÁRIO E EFETUANDO AS DEVIDAS VALIDAÇÕES

while error:

    try:
        # TENTA EFETUAR A CONVERSÃO DOS VALORES
        f_numero_a      = float(input(f"Digite o primeiro número ({f_numero_a}): ") or f_numero_a) 
        f_numero_b      = float(input(f"Digite o segundo número ({f_numero_b}): ") or f_numero_b)
        error = False
    except ValueError:
        # CASO DEU ERRO, APRESENTA A MENSAGEM DE ERRO, E VOLTA A PEDIR OS NÚMEROS
        print("Deve-se digitar um número real válido")
        error = True
        continue
        

    str_operador = input("Digite o operador matemático (+) (-) (/) (*): ")
    if  str_operador not in ["+", "-", "/", "*"]:
        print("O operador matemático não é válido digite: + ou - ou * ou /")
        error = True
    else:
        error = False

# VERIFICA QUAL SERÁ A OPERAÇÃO A SER EXECUTADA
if str_operador == "+":
    resultado = f"O RESULTADO DA SOMA DE {f_numero_a} + {f_numero_b} é: " + str(f_numero_a + f_numero_b)
elif str_operador == "-":
     resultado = f"O RESULTADO DA SUBTRAÇÃO DE {f_numero_a} - {f_numero_b} é: " + str(f_numero_a - f_numero_b)
elif str_operador == "/":
    try:
        resultado = f"O RESULTADO DA DIVISÃO DE {f_numero_a} / {f_numero_b} é: " + str(f_numero_a / f_numero_b)
    except ZeroDivisionError:
        print("Nenhum número pode ser dividido por zero")
        resultado = None
elif str_operador == "*":
    resultado = f"O RESULTADO DA MULTIPLICAÇÃO DE {f_numero_a} * {f_numero_b} é: " + str(f_numero_a * f_numero_b)
else:
    print("Operador não encontrado")
    resultado = None

# APRESENTA O RESULTADO EM TELA
if(resultado != None):
    print("****************************")
    print(resultado)
    print("****************************")