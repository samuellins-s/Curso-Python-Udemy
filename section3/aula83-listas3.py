'''
Métodos úteis:
    append -> adiciona um item ao final
    insert -> adiciona um item no indice escolhido
        dois argumentos: (indice, o que será adicionado) -> insert(0, 'Olá')
    pop -> remove do final ou no indice escolhido
    del -> apaga um indice
    clear -> limpa a lista
    extend -> estende a lista
    + -> concatena listas

'''
lista = [1, 2, 3, 4, 5]

lista.append('Luiz') # adiciona ao final
print(lista)

lista.pop() # retira no final
print(lista)

lista.insert(0, 'Olá') # no indice 0, adicionar 'Olá'. os indices são somados para frente
print(lista)

lista.clear() # limpa a lista
print(lista)
