from model.produto import Produto

class ItemEstoque:
    def __init__(self,
                 id:int=None,
                 id_estoque:int=None,
                 id_produto:float=None,
                 estante:str=None,
                 prateleira:int=None,
                 produto:Produto=None
                 ):
        self.id = id
        self.id_estoque = id_estoque
        self.id_produto = id_produto
        self.estante = estante
        self.prateleira = prateleira
        self.produto = produto

    def get_id_estoque(self):
        return self.id_estoque

    def set_id_estoque(self, id_estoque):
        self.id_estoque = id_estoque

    def get_id_produto(self):
        return self.id_produto

    def set_id_produto(self, id_produto):
        self.id_produto = id_produto

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_prateleira(self):
        return self.prateleira

    def set_prateleira(self, prateleira):
        self.prateleira = prateleira

    def get_produto(self):
        return self.produto

    def set_produto(self, produto):
        self.produto = produto

    def to_string(self):
        # Cria uma representação em string do objeto
        return f"ID Estoque: {self.id_estoque}\nID Produto: {self.id_produto}\nEstante: {self.estante}\nPrateleira: {self.prateleira}\nProduto:\n{self.produto.to_string()}"