class Estoque:
    def __init__(self, 
                 id:int=None, 
                 tipo:str=None
                ):
        self.set_ID(id)
        self.set_tipo(tipo)

    def set_id(self, id:int):
        self.id = id

    def set_tipo(self, tipo:str):
        self.tipo = tipo

    def get_id(self) -> int:
        return self.ID

    def get_tipo(self) -> str:
        return self.tipo

    def to_string(self) -> str:
        return f"ID: {self.get_id()} | Tipo: {self.get_tipo()}"