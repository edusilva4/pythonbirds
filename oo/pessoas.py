class Pessoas:
    olhos = 2
    def __init__(self,*filhos, nome="Null", idade= "Null"):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return "Olá mundo cruel"
    def trabalhar(self):
        return "Meu trabalho é bom"



p = Pessoas("Rafael",37)
print(p.cumprimentar(), p.trabalhar())
print(p.nome)
p.nome = "Eduardo"
print(p.nome,p.idade)

eduardo = Pessoas(nome="Eduardo")
julio = Pessoas(eduardo, nome="Rafael")
for filho in julio.filhos:
    print(filho.nome)

eduardo.sobrenome = "Santos Silva"
print(eduardo.sobrenome)
print(eduardo.__dict__)
print(julio.__dict__)

print(Pessoas.olhos)
print(eduardo.olhos)
print(id(eduardo.olhos))
print(id(julio.olhos))