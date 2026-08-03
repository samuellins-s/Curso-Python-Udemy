'''
Faça um jogo para o usuário adivinhar qual a palavra secreta:

    Você vai propor uma palavra secreta qualquer e vai dar a probabilidade para o usuário digitar apenas uma letra.

    Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        Se a letra digitada estiver na palavra secreta; exiba a letra.
        Se a letra digitada não estiver na palavra secreta; exiba *.
    
    Faça a contagem de tentativas do seu usuário.

'''

# Tentativa de Solução:

'''
Ter uma palavra predefinida pelo programa

input para o usuario digitar apenas uma letra
    tratamento do input:
        1. apenas letras
        2. apenas uma letra.

Se a letra estiver na palavra: exibir a letra acertada com asteriscos. Ex: a -> *a*a** (macaco)

Se a letra não estiver na palavra: exibir apenas os asteriscos.

Fazer a contagem de tentativas do usuario

'''

palavra_secreta = 'macaco'

while True:

    letra_usuario = input('Digite apenas uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra!')
        continue

    # for i in range(palavra_secreta):
    #     ...

    if letra_usuario in palavra_secreta:
        print(letra_usuario)

    if letra_usuario not in palavra_secreta:
        print('*')
        continue

