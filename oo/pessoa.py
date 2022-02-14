class Pessoa :
    def __init__(self, *filhos , nome=None, idade=43 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá '

if __name__ == '__main__':
    melina = Pessoa(nome='Melina')
    gustavo = Pessoa(melina, nome='Gustavo')
    print(Pessoa.cumprimentar(gustavo))
    print(gustavo.cumprimentar())
    print(gustavo.nome)
    print(gustavo.idade)
    for filho in gustavo.filhos:
        print(filho.nome)
    gustavo.sobrenome = 'Gomide'
    del gustavo.filhos
    print(gustavo.__dict__)
    print(melina.__dict__)

