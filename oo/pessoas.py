class Pessoas:
    def __init__(self, nome="Null", idade ="Null"):
        self.nome = nome
        self.idade = idade
    def cumprimentar(self):
        return "Olá mundo cruel"
    def trabalhar(self):
        return "Meu trabalho é bom"
    def calcular(self):
        return

p = Pessoas("Rafael",37)
print(p.cumprimentar(), p.trabalhar())
print(p.nome)
p.nome = "Eduardo"
print(p.nome,p.idade)