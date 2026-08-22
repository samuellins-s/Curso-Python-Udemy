'''
Higher Order Functions
Funções de primeira classe

'''

def saudacao(arg):
    return arg

saudacao_2 = saudacao

# --------------------------------------------

def saudacaoo(msg, nome):
    return f'{msg}, {nome}!'

def execucao(funcao, *args):
    return funcao(*args)

print(
    execucao(saudacaoo, 'Bom dia', 'Luiz')
)

print(
    execucao(saudacaoo, 'Boa noite', 'Maria')
)