class Produto:
    def __init__(self, 
                 id:int=None,
                 nome:str=None,
                 descricao:str=None,
                 quantidade:int=None,
                 categoria:str=None,
                 preco_unitario:float=None,
                 quantidade_reposicao:int=None
                 ):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_nome(nome)
        self.set_quantidade(quantidade)
        self.set_categoria(categoria)
        self.set_preco_unitario(preco_unitario)
        self.set_quantidade_reposicao(quantidade_reposicao)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, quantidade):
        self._quantidade = quantidade

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_preco_unitario(self):
        return self._preco_unitario

    def set_preco_unitario(self, preco_unitario):
        self._preco_unitario = preco_unitario

    def get_quantidade_reposicao(self):
        return self._quantidade_reposicao

    def set_quantidade_reposicao(self, quantidade_reposicao):
        self._quantidade_reposicao = quantidade_reposicao
    
    def to_string(self):
        return f"Descrição: {self.descricao}\nNome: {self.nome}\nQuantidade: {self.quantidade}\nCategoria: {self.categoria}\nPreço Unitário: {self.preco_unitario}\nQuantidade Reposição: {self.quantidade_reposicao}"
    