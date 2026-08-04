'''
For + Range

range -> range(start, stop, step)

O for já faz o índice i += 1 automaticamente

O stop é: stop - 1

'''

numeros = range(10)

for i in numeros:
    print(i)        # 0 ao 9

print('------------------------------------------')

numeros = range(0, 10)

for i in numeros:
    print(i)        # 0 ao 9 

print('------------------------------------------')

numeros = range(0, 10, 2)

for i in numeros:
    print(i)        # 0 ao 9 pulando de 2 em 2

print('------------------------------------------')

numeros = range(10, 0, -1)

for i in numeros:
    print(i)        # 10 ao 1, passo -1

print('------------------------------------------')