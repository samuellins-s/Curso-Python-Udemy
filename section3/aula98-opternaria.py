'''
Operação ternária (condição de uma linha)
<valor> if <condição> else <outro valor>

'''

variavel = 'Valor' if False else 'Outro valor' # printa Valor se verdadeiro, se falso, printa Outro valor

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

# ultimos dois dígitos do CPF

digito = 9
novo_digito = digito if digito <= 9 else 0 # printar digito se menor igual que 9, se não 0
print(novo_digito)