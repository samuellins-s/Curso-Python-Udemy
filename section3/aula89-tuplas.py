'''
Tipo Tupla -> uma lista imutável
É mais rápida que uma lista

    Sem colchetes ou com parenteses

Conseguimos acessar os indices[], mas não mudá-los.

'''

tupla = 'Maria', 'Helena', 'Luiz'
tupla2 = ('Maria', 'Helena', 'Luiz')

# conversão list -> tuple; ou o inverso
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
print(nomes)