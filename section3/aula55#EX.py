"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    if int(numero_inteiro) % 2 == 0:
        print('Esse número é par!')
    else:
        print('Esse número é ímpar!')

else:
    print('Esse número não é inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Digite a hora: '))

if 0 < hora < 11:
    print('Bom dia!')
elif 12 < hora < 17:
    print('Boa tarde!')
else:
    print('Boa boite!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Digite o seu primeiro nome: ')
tamanho_nome = len(primeiro_nome)

if tamanho_nome <= 4:
    print('O seu nome é pequeno.')
elif tamanho_nome == 5 or tamanho_nome == 6:
    print('O seu nome é médio.')
else:
    print('O seu nome é muito grande.')