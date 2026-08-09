'''
enumerate -> enumera iteráveis (índices)

Quando o enumerate é usado 1 vez, ele puxa todos os valores
    Se tentar puxar novamente depois, a lista fica VAZIA.

'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

lista_enumerada = enumerate(lista)
print(lista_enumerada) # entrega local de memoria

for i in lista_enumerada:
    print(i)

for i in lista_enumerada:
    print(i) # valores esgotados - não retorna nada

# PARA CONTORNAR: fazer direto

for i in enumerate(lista):
    print(i)

for i in enumerate(lista):
    print(i)

# ou

lista_enumerada = list(enumerate(lista)) # retorna a lista
print(lista_enumerada)

lista_enumerada = list(enumerate(lista, start=1)) # o indice começa do 1
print(lista_enumerada)

# com desempacotamento

for i in enumerate(lista):
    indice, nome = i
    print(indice, nome)

# OU, MELHOR FORMA:

for indice, nome in enumerate(lista):
    print(indice, nome)