# while = enquanto

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print(f'O seu nome é {nome}')
    
    if nome == 'sair':
        print('Saindo do programa...')
        break # para o laço

while True:
    ...
    
print('acabou') # trecho unreachable (inalcançável). Pois o laço é infinito.