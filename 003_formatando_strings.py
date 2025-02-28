'''
PROGRAMA: FORMATANDO STRINGS EM PYTHON
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: EFETUAR A FORMATAÇÃO DE STRINGS COM PYTHON

COMANDOS:
PRINT   = IMPRIME EM TELA DO QUE FOI CALCULADO
UPPER   = COLOCA O TEXTO EM MAIUSCULO
LOWER   = COLCOA O TEXTO EM MINUSCULO
TITLE   = COLOCA O TEXTO COM AS PRIMEIRAS LEGRAS EM MAIUSCULO
RSTRIP  = REMOVE OS ESPAÇOS, DO LADO DIREITO, DA STRING
LSTRIP  = REMOVE OS ESPAÇOS, DO LADO ESQUERDO, DA STRING
STRIP   = REMOVE OS ESPAÇOS, DO INICIO E FIM, DA STRING

'''

# Declaração da variável
str_texto_curto = " eSTou AprendendO foRMataR teXTos com PYTHON "
str_texto_entre = "*****"

# Concatenar as duas strings e apresentar em tela
print(str_texto_entre + str_texto_curto + str_texto_entre)

# Removendo o espaço do fim do texto
print(str_texto_entre + str_texto_curto.rstrip() + str_texto_entre)

# Removendo o espaço do inicio do texto
print(str_texto_entre + str_texto_curto.lstrip() + str_texto_entre)

# Removendo o espaço do inicio e Fim do texto
print(str_texto_entre + str_texto_curto.strip() + str_texto_entre)

# Tornando o texto todo maiusculo
print(str_texto_entre + str_texto_curto.upper() + str_texto_entre)

# Tornando o texto todo minusculo
print(str_texto_entre + str_texto_curto.lower() + str_texto_entre)

# Tornando o texto tipo título
print(str_texto_entre + str_texto_curto.title() + str_texto_entre)
