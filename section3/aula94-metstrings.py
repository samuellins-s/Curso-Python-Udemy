'''
split -> divide uma string (fatia) em uma lista
strip -> corta os espaços inicial e final de uma str
    lstrip -> somente o espaço da esquerda (left)
    rstrip -> somente o espaço da direita (right)

join -> une uma string    
    
'''

frase = 'Olha só que, coisa interessante!'
lista_palavras = frase.split()
print(lista_palavras) # ['Olha', 'só', 'que', 'coisa', 'interessante!']

for i in lista_palavras:
    print(i)

lista_frases = frase.split(',')
print(lista_frases)

# -------------------------------------------------

frase2 = ' Opa, cortando os dois espaços. '
print(frase2.strip())

# -------------------------------------------------

frase3 = '-'.join('abc')
print(frase3) # a-b-c

frase4 = 'Olá, Tudo bem?'
frase5 = 'Sim! Tudo certo.'
frases4_e_5 = frase4, frase5

frases_unidas = '-'.join(frases4_e_5)
print(frases_unidas) # Olá, Tudo bem?-Sim! Tudo certo.