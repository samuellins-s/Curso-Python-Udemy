'''
Convensão sobre valores constantes (valores que não devem ser mudados):
    Escrever em letras MAIÚSCULAS

'''
RADAR_1 = 60 # km máximo do radar 1
LOCAL_1 = 100 # onde o radar 1 está
RADAR_RANGE = 1 # range que o radar pega

# carro atual

velocidade_do_carro = 61
local_carro = 100

# saber se o carro passou na velocidade permitida do radar

if local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE) and velocidade_do_carro > RADAR_1:
    print('O carro foi multado no radar 1 por excesso de velocidade')