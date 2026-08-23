'''
Crie funções que duplicam, triplicam e quadruplicam o nº recebido como parâmetro

'''

def criar_multiplicoes(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicoes(2)
triplicar = criar_multiplicoes(3)
quadruplicar = criar_multiplicoes(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))