from conexion.oracle_queries import OracleQueries
from view import menu

class SplashScreen:
    def __init__(self):
        self.qry_total_produto = menu.QUERY_COUNT.format(tabela="produto")
        self.qry_total_estoque = menu.QUERY_COUNT.format(tabela="estoque")
        self.qry_total_item_estoque = menu.QUERY_COUNT.format(tabela="item_estoque")

        self.created_by = """
                    FABIO GONÇALVES, 
                    MARCELO MIRANDA,
                    NICOLAS RODRIGUES
                    THIAGO MELO"""
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"
        
    def get_total_estoque(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_estoque)["total_estoque"].values[0]

    def get_total_produto(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_produto)["total_produto"].values[0]


    def get_total_item_estoque(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_item_estoque)["total_item_estoque"].values[0]


    def get_updated_screen(self):
        return(
        f"""
        =-=-=-=-=-=-=-=-=-=-=-=-= GESTÃO DE ESTOQUE =-=-=-=-=-=-=-=-=-=-=-=-=
        
            Total de registros existentes:
                1 - ESTOQUE:                {str(self.get_total_estoque()).rjust(5)}
                2 - PRODUTO:                {str(self.get_total_produto()).rjust(5)}
                3 - ITEM_ESTOQUE:           {str(self.get_total_item_estoque()).rjust(5)}
            
            ------------------------------------
            Criado por: {self.created_by}

            Professor: {self.professor}
            
            DISCIPLINA: {self.disciplina}
                        {self.semestre}
            ------------------------------------

        {"=-=" * 23}
        """
        )