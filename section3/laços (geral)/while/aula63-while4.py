'''
Pular um loop = continue

'''
contador = 0

while contador <= 10:
    contador += 1

    if contador == 6:
        continue # quando tiver o continue, ele pula e não executa

    print(contador)

print(30*'-')

contador = 0

while contador <= 100:
    contador += 1

    if contador >= 30 and contador <= 70:
        continue

    print(contador)