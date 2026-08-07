'''
Faça uma lista de compras com listas
    list

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
    insert/append, del/pop, enumerate(list)

Não permita que o programa quebre com erros de índices inexistentes na lista
    lista_enumerada = list(enumerate(lista))
    for indice, item in list(enumerate(lista))
        print(indice, item)
'''

lista_compras = []

nome_usuario = input('Digite o seu nome: ')

print(f'Olá! {nome_usuario}. A sua lista de compras é: {lista_compras}')