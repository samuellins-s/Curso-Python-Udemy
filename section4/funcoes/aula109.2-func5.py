'''
Função dentro de função
Global (manipula o que está fora do escopo)

'''

x = 1

def escopo():
    global x # manipula o x externo
    x = 10 # esse x só existe dentro da func escopo()

    def outra_função():
        x = 100 # esse outro x só existe dentro dessa func

        y = 2
        print(x, y)

    outra_função()
    print(x)

escopo()
print(x) # o x foi manipulado (global)