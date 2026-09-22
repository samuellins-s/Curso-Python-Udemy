'''
Métodos de classe + factories(fábricas)

São métodos onde "self" será "cls", ou seja, ao invés de receber a instancia no primeiro parametrom recebemos a propria classe.

'''

class PessoaSemClassmethod:
    ano = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_de_classe(self):
        print('hey')

p1 = PessoaSemClassmethod('João', 16)
p1.metodo_de_classe() # precisa instanciar para usar

# -------------------------@CLASSMETHODS----------------------------

class Pessoa:
    ano = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)

Pessoa.metodo_de_classe()

p2 = Pessoa.criar_com_50_anos('Josefa')
print(p2.nome, p2.idade)

p3 = Pessoa.criar_sem_nome(30)
print(p3.nome, p3.idade)