'''
Imprecisão do ponto flutuante
    Solução 1 -> Formatação (:.xf)

'''

# exemplo

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2
print(numero3) # 0.7999999999999999 (valor impreciso)
print(f'{numero3:.2f}') # 0.80

print(round(numero3, 2)) # arredonda