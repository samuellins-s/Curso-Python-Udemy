'''
Qual letra apareceu mais vezes na frase a seguir?

'''

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.' # as contrabarras (\) continuam a frase

print(frase.count('Python')) # Ou seja, conta quantas vezes Python aparece na frase

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    i += 1

    print(letra_atual, qtd_apareceu_mais_vezes_atual)