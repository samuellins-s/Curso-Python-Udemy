'''
Sempre quando tiver um input para o usuario, é preciso tratar esse valor

Se tiver um erro no try, vai para o except imediatamente (fail fast)
    Na linha que der erro, já vai para o except continuamente

'''
numero_string = input('Vou dobrar o número que você digitar: ')

try:
    print('String:', numero_string)
    numero_float = float(numero_string) # converte de str para float
    print('Float:', numero_float)
    print(f'O dobro de {numero_string} é: {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
