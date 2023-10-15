from conexion.oracle_queries import OracleQueries

class Relatorio:

    def get_produto_todos_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_todos_produtos = "SELECT * FROM produto ORDER BY (id)"

        print("\n")
        print(oracle.sqlToDataFrame(query_produto_todos_produtos))
        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    
    def get_produto_valor_total(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_valor_total = """SELECT SUM(preco_unitario * quantidade) as "Soma" FROM produto ORDER BY (id)"""
        
        print("\n")
        print(oracle.sqlToDataFrame(query_produto_valor_total))
        input("\nPressione Enter para Sair do Relatório de Produtos ")

    
    def get_produto_produtos_reposicao(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_reposicao = "SELECT * FROM produto where quantidade <= quantidade_reposicao ORDER BY (id)"

        print("\n")
        print(oracle.sqlToDataFrame(query_produto_reposicao))
        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    
    def get_estoque_todos_estoques(self):
        oracle = OracleQueries()
        oracle.connect()
        query_estoque_todos_estoques = "SELECT * FROM estoque ORDER BY (id)"

        print("\n")
        print(oracle.sqlToDataFrame(query_estoque_todos_estoques))
        input("\nPressione Enter para sair do Relatório de Estoque ")
        
    
    def get_estoque_produto_em_estoque_especifico(self):
        id_estoque = int(input("Informe o id do estoque: "))

        oracle = OracleQueries()
        oracle.connect()
        query_estoque_produto_em_estoque_especifico = f"""
            SELECT p.*
            FROM item_estoque ie
            INNER JOIN produto p
            on ie.id_produto = p.id and ie.id_estoque = {id_estoque}
            ORDER BY (p.id)
            """

        print("\n")
        print(oracle.sqlToDataFrame(query_estoque_produto_em_estoque_especifico.format(id_estoque = id_estoque)))
        input("\nPressione Enter para sair do Relatório de Estoque ")

    
    def get_item__todos_itens(self):
        oracle = OracleQueries()
        oracle.connect()
        query_item__todos_itens = "SELECT * FROM item_estoque ORDER BY (id)"

        print("\n")
        print(oracle.sqlToDataFrame(query_item__todos_itens))
        input("\nPressione Enter para sair do Relatório de Itens ")

    
    def get_item_localizacao_produto_especifico(self):
        id_produto = int(input("Informe o id do produto: "))

        oracle = OracleQueries()
        oracle.connect()
        query_item_localizacao_produto_especifico = """
            SELECT distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            FROM produto p
            INNER JOIN item_estoque i
                on i.id_produto = p.id
            where i.id_produto = {id_produto}
            """

        print("\n")
        print(oracle.sqlToDataFrame(query_item_localizacao_produto_especifico.format(id_produto=id_produto)))
        input("\nPressione Enter para sair do Relatório de Itens ")