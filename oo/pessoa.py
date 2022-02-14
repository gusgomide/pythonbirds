class Pessoa :
    olhos = 2
    def __init__(self, *filhos , nome=None, idade=43 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá '

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classs(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    gustavo.olhos = 1
    del gustavo.olhos
    print(gustavo.__dict__)
    print(melina.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(gustavo.olhos)
    print(melina.olhos)
    print(Pessoa.metodo_estatico(), gustavo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classs(), gustavo.nome_e_atributos_de_classs())

