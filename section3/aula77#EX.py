'''
Faça um jogo para o usuário adivinhar qual a palavra secreta:

    Você vai propor uma palavra secreta qualquer e vai dar a probabilidade para o usuário digitar apenas uma letra.

    Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
        Se a letra digitada estiver na palavra secreta; exiba a letra.
        Se a letra digitada não estiver na palavra secreta; exiba *.
    
    Faça a contagem de tentativas do seu usuário.

'''

# Lógica Solução:

'''
Ter uma palavra predefinida pelo programa

input para o usuario digitar apenas uma letra
    tratamento do input:
        1. apenas letras
        2. apenas uma letra.

Se a letra estiver na palavra: exibir a letra acertada com asteriscos. Ex: a -> *a*a** (macaco)
    concatenar:
        letra acertada em letra usuario


Se a letra não estiver na palavra: exibir apenas os asteriscos.

Fazer a contagem de tentativas do usuario

'''

palavra_secreta = 'macaco'
letras_acertadas = ''
numero_tentativas = 0

while True:

    letra_usuario = input('Digite apenas uma letra: ')

    numero_tentativas += 1

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palava_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palava_formada += letra_secreta

        else:
            palava_formada += '*'

    print(palava_formada)

    if palava_formada == palavra_secreta:
        print('VOCÊ GANHOU!! PARABÉNS')
        print('A palavra secreta era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)