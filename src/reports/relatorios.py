from conexion.oracle_queries import OracleQueries

class Relatorio:

    def get_produto_todos_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_todos_produtos = "select * from produto"

        print("\n")
        print(oracle.sqlToDataFrame(query_produto_todos_produtos))
        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    def get_produto_valor_total(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_valor_total = """select SUM(preco_unitario * quantidade) as "Soma" from produto"""
        
        print("\n")
        print(oracle.sqlToDataFrame(query_produto_valor_total))
        input("\nPressione Enter para Sair do Relatório de Produtos ")

    def get_produto_produtos_reposicao(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_reposicao = "select * from produto where quantidade <= quantidade_reposicao"

        print("\n")
        print(oracle.sqlToDataFrame(query_produto_reposicao))
        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    def get_estoque_todos_estoques(self):
        oracle = OracleQueries()
        oracle.connect()
        query_estoque_todos_estoques = "select * from estoque"

        print("\n")
        print(oracle.sqlToDataFrame(query_estoque_todos_estoques))
        input("\nPressione Enter para sair do Relatório de Estoque ")
        
    def get_estoque_produto_em_estoque_especifico(self):
        id_estoque = int(input("Informe o id do estoque: "))

        oracle = OracleQueries()
        oracle.connect()
        query_estoque_produto_em_estoque_especifico = """
            select p.*
            from item_estoque ie
            inner join produto p
            on ie.id_produto = p.id and ie.id_estoque = {id_estoque}
            """

        print("\n")
        print(oracle.sqlToDataFrame(query_estoque_produto_em_estoque_especifico.format(id_estoque = id_estoque)))
        input("\nPressione Enter para sair do Relatório de Estoque ")

    def get_item__todos_itens(self):
        oracle = OracleQueries()
        oracle.connect()
        query_item__todos_itens = "select * from item_estoque"

        print("\n")
        print(oracle.sqlToDataFrame(query_item__todos_itens))
        input("\nPressione Enter para sair do Relatório de Itens ")

    def get_item_localizacao_produto_especifico(self):
        id_produto = int(input("Informe o id do produto: "))

        oracle = OracleQueries()
        oracle.connect()
        query_item_localizacao_produto_especifico = """
            select distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            from produto p
            inner join item_estoque i
                on i.id_produto = p.id
            where i.id_produto = {id_produto}
            """

        print("\n")
        print(oracle.sqlToDataFrame(query_item_localizacao_produto_especifico.format(id_produto=id_produto)))
        input("\nPressione Enter para sair do Relatório de Itens ")