'''
Manipulando chaves e valores em dicionários
CRUD

Método .get verifica se uma chave existe
    Por padrão, se não existir, retorna None
    Usada em if's (condicionais)

'''

pessoa = {}

pessoa['nome'] = 'Luiz Otávio'

print(pessoa) # tudo
print(pessoa['nome']) # Luiz Otávio

# criar dinamicamente:

chave = 'nome' # em variavel

pessoa[chave] = 'Samuel'
pessoa['sobrenome'] = 'Lins'

print(pessoa[chave]) # acessando a variavel
del pessoa['sobrenome'] # é possível apagar valores DEL
print(pessoa)

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE SOBRENOME')
else:
    print(pessoa['sobrenome'])