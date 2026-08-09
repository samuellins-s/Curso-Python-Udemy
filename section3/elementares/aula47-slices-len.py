'''
Strings são iteráveis

 012345678
 Olá mundo
-987654321

Fatiamento [inicio:fim:passo], ou seja, [i:f:p]
Função len: retorna a quantidade

'''

variavel = 'Olá mundo'

print(variavel[5]) # u 
print(variavel[-4]) # u

print(20*'-')

print(variavel[4:]) # 4 até o fim (mundo)
print(variavel[4:8]) # 4 até o índice 8-1 (mund)

print(20*'-')

print(variavel[:5]) # início até o índice 5-1 (Olá m)
print(variavel[-8:-2]) # 8 até -2-1 (lá mun)

print(20*'-')

print(len(variavel)) # int 9
print(variavel[0:len(variavel):1]) # ínicio até o fim da variavel, passo de 1 em 1
print(variavel[0:len(variavel):2]) # passo de 2 em 2
print(variavel[::-1]) # incío ao fim, passo -1 inverte