'''
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Carlos')

for i in range(len(lista)):
    print(i, lista[i])