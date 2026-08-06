'''
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)

'''
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy() # lista_b é uma cópia da lista_a

lista_a[0] = 'Qualquer coisa' # alterei apenas a lista_a
print(lista_a)
print(lista_b)