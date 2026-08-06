'''
Listas são mutáveis
Função list
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete (CRUD)
Criar, Ler, Alterar, Apagar = lista[i] (CRUD)

'''

lista = [10, 20, 30, 40]
lista[2] = 300 # lista é mutável. alterei o valor do índice 2
print(lista[2])
print(lista) # o valor é alterado.

'''
Deletar (del) um indice: 
    O python reorganiza a lista (indices)
Fato importante do del no meio de listas grandes: 
    Requer muito processamento. Movimenta todos os números e os íncices também
'''
lista2 = [1, 2, 3, 4, 5]
del lista2[0] # indice 0 (1) é apagado e a lista2 é reorganizada
print(lista2)
print(lista2[0]) # 2 é indice 0

'''
.append(): adicionar ao final da lista
'''
lista3 = [1, 2, 3, 4, 5]
lista3.append(6) # adiciona 6 ao final da lista3
print(lista3)

'''
.pop(): remove ao final da lista
    pop(3) = remove o indice 3 da lista
'''
lista3.pop() # remove o ultimo item (6) da lista3
print(lista3)
lista3.pop(1) # remove o indice 1 (2)
print(lista3)