'''
Qual letra apareceu mais vezes na frase a seguir?

'''

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.' # as contrabarras (\) continuam a frase

print(frase.count('Python')) # Ou seja, conta quantas vezes Python aparece na frase

# teste

# i = 0

# while i < len(frase):
#     letra_atual = frase[i]
#     i += 1

#     if letra_atual == ' ':
#         i += 1
#         continue

#     print(letra_atual)

# exercicio em si

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letra = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

        
    
    print(letra_atual, qtd_letra)

    i += 1