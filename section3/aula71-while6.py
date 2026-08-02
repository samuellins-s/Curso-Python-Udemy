'''
Qual letra apareceu mais vezes na frase a seguir?

'''

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.' # as contrabarras (\) continuam a frase

print(frase.count('Python')) # Ou seja, conta quantas vezes Python aparece na frase

'''
Analisar as letras atuais:

Variavel: maior
se a qtd letra atual for maior que a anterior: a letra atual continua sendo a maior

se a qtd letra atual for menor que a anterior: a letra anterior continua sendo a maior

sempre salvar a letra atual na memoria e compara com a anterior

variaveis:

    1. quantidade (memoria) 
    2. quantidade atual 

    fica looping em que compara a qtd na memoria e a atual pelo "i"
    
'''
i = 0
qtd_letra_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_letra_apareceu_mais_vezes < qtd_letra_atual:
        qtd_letra_apareceu_mais_vezes = qtd_letra_atual
        letra_apareceu_mais_vezes = letra_atual
    
    i += 1

print(f'A letra "{letra_apareceu_mais_vezes}" apareceu {qtd_letra_apareceu_mais_vezes} vezes.')