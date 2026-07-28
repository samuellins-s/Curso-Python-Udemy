'''
Calculadora com While

Pedir o primeiro e segundo valor ao usuário
Perguntar qual o operador (+, -, *, /)
Mostrar o resultado da operação (primeiro com o segundo)

'''

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    # validação dos números

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        print('Um ou ambos os números digitados são inválidos!')
        continue

    # validação do operador

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador!')
        continue
    
    # operação em si

    if operador == '+':
        resultado = numero_1_float + numero_2_float
        print(f'Resultado: {numero_1_float} + {numero_2_float} = {resultado}')
    elif operador == '-':
        resultado = numero_1_float - numero_2_float
        print(f'Resultado: {numero_1_float} - {numero_2_float} = {resultado}')
    elif operador == '/':
        resultado = numero_1_float / numero_2_float
        print(f'Resultado: {numero_1_float} / {numero_2_float} = {resultado}')
    elif operador == '*':
        resultado = numero_1_float * numero_2_float
        print(f'Resultado: {numero_1_float} * {numero_2_float} = {resultado}')

    # comando sair ou não
    
    sair = input('Você deseja sair? [s] ou [n]: ').lower()
    
    if sair == 's':
        break
    elif sair =='n':
        continue
    else:
        print('Digite [s] ou [n]')
        sair = input('Você deseja sair? [s] ou [n]: ')

