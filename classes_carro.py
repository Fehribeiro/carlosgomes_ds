class Carros:
    def __init__(self, marca, modelo, cor, ano, valor):
        self.marca=marca
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        self.valor=valor

class Tipo:
    def __init__(self, modelo, cor, motor, rodas):
        

class Estoque:
    def __init__(self):
        self.carros=[]
    def Adicionar_Carros(self,carro): 
        self.carros.append(carro)
    def Mostrar_Estoque(self):
        for carro in self.carros:
            print(f"{carro.modelo}, {carro.marca}: adicionado ao estoque")

carro_1=Carros("Chevrolet", "Corsa", "Bege", "2007", 15000)
carro_2=Carros("Wolkswagem", "Gol", "Verde", "2006", 12000)
carro_3=Carros("Honda", "Civic", "Branco", "2020", 70000)

estoque=Estoque()
estoque.Adicionar_Carros(carro_1)
estoque.Adicionar_Carros(carro_2)
estoque.Adicionar_Carros(carro_3)

estoque.Mostrar_Estoque()


