'''
O While é usado para quando não se sabe quantas repeticões terão.

For + in

'''

texto = 'Python'

for letra in texto:
    print(letra)

# ------------------------------------------

texto = 'Python'

texto_com_asteriscos = ''

for i in texto:
    texto_com_asteriscos += i + '*'

print('*' + texto_com_asteriscos)