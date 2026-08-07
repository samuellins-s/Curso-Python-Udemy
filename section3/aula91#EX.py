'''
Faça uma lista de compras com listas
    list

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
    append, del, enumerate(list)

Não permita que o programa quebre com erros de índices inexistentes na lista
    lista_enumerada = list(enumerate(lista))
    for indice, item in list(enumerate(lista))
        print(indice, item)
'''

import os

lista_compras = []

while True:
    mensagem_principal = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar [s]air: ')

    if mensagem_principal == 'i':
        os.system('cls')
        inserir = input('Opção [i]nserir escolhida\nDigite o que você quer inserir: ')
        lista_compras.append(inserir)
        continue

    elif mensagem_principal == 'a':
        os.system('cls')
        deletar = input('Opção [a]pagar escolhida\nDigite qual índice você quer deletar: ')

        if len(deletar) > 1:
            print('\nDigite apenas 1 índice por vez\n')
            continue
        
        if not deletar.isdigit():
            print('\nDigite apenas um número!\n')
            continue

        try:
            

        deletar_indice_int = int(deletar)
        del lista_compras[deletar_indice_int]
        continue

    elif mensagem_principal == 'l':
        os.system('cls')

        if len(lista_compras) == 0:
            print(f'Opção [l]istar escolhida\n')
            print('Lista vazia!\n')

        print(f'Opção [l]istar escolhida\nConfira a sua lista a seguir:\n')

        for indice, item in enumerate(lista_compras):
            print(indice, item)

        print()
        continue

    elif mensagem_principal == 's':
        os.system('cls')
        print('Opção [s]air escolhida\nObrigado, volte sempre!')
        break

    else:
        print('Selecione uma das opções anteriores.\n')
        continue