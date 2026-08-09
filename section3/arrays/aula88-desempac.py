'''
Introdução ao desempacotamento + tuples (tuplas)

'''

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2) # Helena

'''
Se a quantidade de variaveis for menor que os valores: ERRO!!!
    o contrario também dá erro.
    qtd_variaveis = qtd_valores
    ValueError

nome1, nome2 = ['Maria', 'Helena', 'Luiz']  ERRO!!!
nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']  ERRO!!!

'''

# resto = com asterisco (*variavel) = empacotamento do resto.
nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1, resto)
# como ela é uma variavel que não é utilizada:
#   conversão: *_
_, nome2, *_ = ['Maria', 'Helena', 'Luiz']
print(nome2)