'''
Dicionários (dict)
Par "Chave" e "Valor".
Usar "{}" ou classe dict para criar dicionário
São mutáveis

'''

pessoa = {
    'nome': 'Samuel',
    'sobrenome': 'Lins',
    'idade': 18,
    'altura': 1.72,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'tal tal', 'número': 123},
    ],
}

print(pessoa['nome']) # acesso pelo indice (string)

for chave in pessoa: # no indice direto (i) -> pega as chaves
    print(chave, pessoa[chave]) # para pegar os valores (pessoa[chave])