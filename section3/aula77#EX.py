'''
Faça um jogo para o usuário adivinhar qual a palavra secreta:

    Você vai propor uma palavra secreta qualquer e vai dar a probabilidade para o usuário digitar apenas uma letra.

    Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        Se a letra digitada estiver na palavra secreta; exiba a letra.
        Se a letra digitada não estiver na palavra secreta; exiba *.
    
    Faça a contagem de tentativas do seu usuário.

'''

palavra_secreta = 'Macaco'

while True:

    letra_usuario = input('Digite apenas uma letra: ')

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra!')
        continue

    for i in range(palavra_secreta):
        ...

    if letra_usuario not in palavra_secreta:
        print('*')
        continue

    if letra_usuario in palavra_secreta:
        print(letra_usuario)

