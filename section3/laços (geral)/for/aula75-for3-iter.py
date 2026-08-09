'''
Iterável: str, range, etc (__iter__)
    método ->  __iter__()

Iterador: quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador

métodos com "__x__" -> método dunder

'''
texto = 'Luiz'.__iter__()   # ação; mostra o endereço de memória onde o iter está
print(texto)

texto2 = iter('João')   # função iter. Mesma coisa do que o método __iter__
print(texto)

# ------------------------------------------

texto3 = iter('Carlos')

print(texto3.__next__())
print(texto3.__next__())
print(texto3.__next__())
print(next(texto3))     # função next. mesma coisa que o método __next__()

    # se acabar as iterações do texto, dá erro: StopIteration

# ------------------------------------------

# for por baixo dos panos:

texto4 = 'Luiz' # iterável
iterador = iter(texto4) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break