'''
PROGRAMA: ESTRUTURAS COM PYTHON -  COMANDO FOR
CRIADOR:  EVERTON WILLIAM CONSTANTINO
OBJETIVO:
    O comando try-except no Python é uma forma de evitar que um erro interrompa o programa. 
    Imagine que você está digitando um número para dividir outro valor, mas, sem querer, coloca um zero, o que causaria um erro. 
    Com try-except, o programa tenta executar a operação e, se houver um erro, ele é capturado e tratado, 
    exibindo uma mensagem amigável em vez de simplesmente travar. 
    Isso torna o código mais seguro e confiável, permitindo que ele continue rodando mesmo quando algo inesperado acontece.

Para ter o acesso a todos os exception, é possível utilizar o seguinte comando:
    import builtins
    print(dir(builtins))
   
'''
# Apresentando o erro padão do Python
f_numero = 0.00
f_resultado = 0.00
#f_numero = float(input("digite um número válido: "))

# Tratando o erro com Try, o programa continua sendo executado
try:
    f_numero = float(input("digite um número válido: "))
except ValueError:
    print("O valor digitado não é um número")
finally:
    print("encerrando o try")
    #exit()

# esta linha continua em execução
print("*** Continuando o programa ***")

#tratando um erro de divisão por zero.
try:
    f_numero        = float(input("digite um número válido: "))
    f_resultado     = f_numero / 0
except ValueError:
    print("O valor digitado não é um número")
except ZeroDivisionError:
    print("O número não pode ser dividido por zero")
finally:
    print("Encerrando o try")
    #exit()


# esta linha continua em execução
print("*** Continuando o programa ***")