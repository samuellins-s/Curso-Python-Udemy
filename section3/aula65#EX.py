''''
iterando strings com while

'''

nome = 'Luiz Otávio'

tamanho_nome = len(nome)

novo_nome = ''
indice = 0

while indice < tamanho_nome:
    letra = nome[indice] + '*'
    novo_nome += letra

    indice += 1

print(f'*{novo_nome}', end='')