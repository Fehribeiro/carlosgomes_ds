class Petshop:
    def __init__(self, nome, endereço, cnpj, email, senha, telefone, site):
        self.nome = nome 
        self.endereço = endereço
        self.cnpj = cnpj
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.site = site

class Produtos(Petshop):
    def __init__(self, quantidade, marca, nome, codigo):
        super().__init__(self.endereço, self.site)
        self.quantidade = quantidade
        self.marca = marca
        self.nome = nome
        self.codigo = codigo
        self.estoque = []
    def add_produto(self,produto):


            
