from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # with open("sql/produto_todos_produtos.sql") as f:
        #     self.query_produto_todos_produtos = f.read()
                
        # with open("sql/produto_valor_total.sql") as f:
        #     self.query_produto_valor_total = f.read()
        
        # with open("sql/produto_reposicao.sql") as f:
        #     self.query_produto_reposicao = f.read()
        
        # with open("sql/estoque_todos_estoques.sql") as f:
        #     self.query_estoque_todos_estoques = f.read()
        
        # with open("sql/estoque_produto_em_estoque_especifico.sql") as f:
        #     self.query_estoque_produto_em_estoque_especifico = f.read()
        
        # with open("sql/item__todos_itens.sql") as f:
        #     self.query_item__todos_itens = f.read()
        
        # with open("sql/item_localizacao_produto_especifico.sql") as f:
        #     self.query_item_localizacao_produto_especifico = f.read()
        

        self.query_produto_todos_produtos = "select * from produto p"
        self.query_produto_valor_total = """select SUM(preco_unitario * quantidade) as "Soma" from produto"""
        self.query_produto_reposicao = "select * from produto where quantidade <= quantidade_reposicao"
        self.query_estoque_todos_estoques = "select * from estoque"
        self.query_estoque_produto_em_estoque_especifico = """
            select p.*
            from item_estoque ie
            inner join produto p
            on ie.id_produto = p.id and ie.id_estoque = {id_estoque}
            """
        self.query_item__todos_itens = "select * from item_estoque"
        self.query_item_localizacao_produto_especifico = """
            select distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            from produto p
            inner join item_estoque i
                on i.id_produto = p.id
            where i.id_produto = {id_produto}
            """


    def get_produto_todos_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")

        print(oracle.sqlToDataFrame(self.query_produto_todos_produtos))
        input("\nPressione Enter para Sair do Relatório de Produtos")
    
    def get_produto_valor_total(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")

        print(oracle.sqlToDataFrame(self.query_produto_valor_total))
        input("\nPressione Enter para Sair do Relatório de Produtos")

    def get_produto_produtos_reposicao(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")

        print(oracle.sqlToDataFrame(self.query_produto_reposicao))
        input("\nPressione Enter para Sair do Relatório de Produtos")
    
    def get_estoque_todos_estoques(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")
        
        print(oracle.sqlToDataFrame(self.query_estoque_todos_estoques))
        input("\nPressione Enter para sair do Relatório de Estoque")
        
    def get_estoque_produto_em_estoque_especifico(self):
        id_estoque = int(input("Informe o id do estoque: "))

        oracle = OracleQueries()
        oracle.connect()
        print("\n")
        
        print(oracle.sqlToDataFrame(self.query_estoque_produto_em_estoque_especifico.format(id_estoque = id_estoque)))
        input("\nPressione Enter para sair do Relatório de Estoque")

    def get_item__todos_itens(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")
        
        print(oracle.sqlToDataFrame(self.query_item__todos_itens))
        input("\nPressione Enter para sair do Relatório de Itens")

    def get_item_localizacao_produto_especifico(self):
        oracle = OracleQueries()
        oracle.connect()
        print("\n")
        
        print(oracle.sqlToDataFrame(self.query_item_localizacao_produto_especifico))
        input("\nPressione Enter para sair do Relatório de Itens")