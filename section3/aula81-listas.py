'''
Listas são mutáveis
Função list
Métodos úteis: append, insert, pop, del, clear, extend, +

'''
#        +01234
#        -54321        
string = 'ABCDE'    # 5 caracteres (len)

#        +0    1          2         3
#        -4   -3         -2        -1
lista = [123, True, 'Luiz Otávio', 1.2]
print(lista)
print(lista[0])

lista_dentro_de_lista = ['Olá', 321, 5.5, ['Lista 2', 2]]
print(lista_dentro_de_lista)
print(lista_dentro_de_lista[-1])

print(lista_dentro_de_lista[0].upper()) # consigo modificar o indice para maiusculo

lista_dentro_de_lista[0] = 'Mudei! Tchau!'
print(lista_dentro_de_lista)