'''
Lista dentro de listas, e seus índices.

'''

salas = [
    #   0
    ['Maria'], # 0
    #   0         1
    ['Elaine', 'Gabriel'], # 1
    #   0         1      2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)] # 2
]

print(salas)

for sala in salas:
    for pessoa in sala:
        print(pessoa)

print(salas[1][0]) # acessa o indice 1 das salas (['Elaine', 'Gabriel']) e depois o indice 0 desta lista (Elaine)
print(salas[0][0])
print(salas[2][3][2]) # 20