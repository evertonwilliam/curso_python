'''
PROGRAMA: CONVERTENDO TIPOS DE VARIAVEIS
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO: EFETUAR A CONVERSÃO DE TIPOS DE VARIÁVEIS

COMANDOS:
float()
int()
str()
'''
# Definindo as variáveis a serem utilizadas
str_nome    = "Nome"
int_idade   = 15
float_valor = 10.5

# apresentando os tipos das variáveis em sua criação
print("A variável str_nome é do tipo: ", type(str_nome))
print("A variável int_idade é do tipo: ", type(int_idade))
print("A variável float_valor é do tipo: ", type(float_valor))

# Convertendo a variável int_idade
int_idade = float(int_idade)
print("A variável int_idade agora é float: ", type(int_idade))

# Convertendo a variável int_idade
float_valor = int(float_valor)
print("A variável int_idade agora é int: ", type(float_valor))

# Convertendo a variável int_idade
int_idade = str(int_idade)
print("A variável int_idade agora é string: ", type(int_idade))
