from datetime import date
class pessoa:
    def __init__(self, nome, datan,nomeMae,nomePai,data=date.today().strftime("%d/%m/%Y")):
        self.nome = nome
        self.nomeMae = nomeMae
        self.nomePai = nomePai
        self.datan = datan
        self.data=data
    
    def idade(self):
        if self.datan[3:5] >= self.data[3:5] and self.datan[0:3] < self.data[0:3]:
            return (int(self.data[6:]) - int(self.datan[6:])-1)
        else:
            return (int(self.data[6:]) - int(self.datan[6:]))

   
    def __str__(self):
        idade = self.idade()
        print("Nome: {}\nMae: {}\nPai:{}\nIdade:{}".format(self.nome,self.nomeMae, self.nomePai,idade))

    

carva = pessoa("rafael","10/05/1974", "Rejane","marcelo")
carva.__str__()


