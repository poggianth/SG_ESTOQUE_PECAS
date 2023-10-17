from conexion.oracle_queries import OracleQueries

class Relatorio:

    def get_produto_todos_produtos(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_todos_produtos = "SELECT * FROM produto ORDER BY (id)"

        print("\n")

        result = oracle.sqlToDataFrame(query_produto_todos_produtos)
        
        if result.empty:
            print("Não existe nenhum produto cadastrado!")
            input("\nPressione Enter para Sair do Relatório de Produtos ")

            return False
        else:
            print("Produtos cadastrados: ")
            print(result)
            input("\nPressione Enter para Sair do Relatório de Produtos ")

            return True

    
    
    def get_produto_valor_total(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_valor_total = """
            SELECT
                ID AS Produto_ID,
                NOME AS Produto_Nome,
                QUANTIDADE AS Quantidade,
                PRECO_UNITARIO AS Preco_Unitario,
                QUANTIDADE * PRECO_UNITARIO AS ValorTotalPorProduto
            FROM
                Produto
            UNION ALL
            SELECT
                NULL AS Produto_ID,
                'Total Geral' AS Produto_Nome,
                NULL AS Quantidade,
                NULL AS Preco_Unitario,
                SUM(QUANTIDADE * PRECO_UNITARIO) AS ValorTotalGeral
            FROM
                Produto
        """
        
        print("\n")

        result = oracle.sqlToDataFrame(query_produto_valor_total)
        if result.empty:
            print("Não existe nenhum produto cadastrado!")
        else:
            print(result)

        input("\nPressione Enter para Sair do Relatório de Produtos ")

    
    def get_produto_produtos_reposicao(self):
        oracle = OracleQueries()
        oracle.connect()
        query_produto_reposicao = "SELECT * FROM produto where quantidade <= quantidade_reposicao ORDER BY (id)"

        print("\n")
        result = oracle.sqlToDataFrame(query_produto_reposicao)
        
        if result.empty:
            print("Nenhum produto precisa de reposição! :)")
        else:
            print(result)

        input("\nPressione Enter para Sair do Relatório de Produtos ")
    
    
    def get_estoque_todos_estoques(self):
        oracle = OracleQueries()
        oracle.connect()
        query_estoque_todos_estoques = "SELECT * FROM estoque ORDER BY (id)"

        print("\n")
        result = oracle.sqlToDataFrame(query_estoque_todos_estoques)
        
        if result.empty:
            print("Não existe nenhum estoque cadastrado!")
            input("\nPressione Enter para sair do Relatório de Estoque ")
            
            return False
        
        else:
            print("Estoques cadastrados: ")
            print(result)
            input("\nPressione Enter para sair do Relatório de Estoque ")
            
            return True

        
    
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
        result = oracle.sqlToDataFrame(query_estoque_produto_em_estoque_especifico)

        if result.empty:
            print(f"Não existe nenhum produto no estoque ({id_estoque})")
        else:
            print(result)
        
        input("\nPressione Enter para sair do Relatório de Estoque ")

    
    def get_item__todos_itens(self):
        oracle = OracleQueries()
        oracle.connect()
        query_item__todos_itens = "SELECT * FROM item_estoque ORDER BY (id)"

        print("\n")
        result = oracle.sqlToDataFrame(query_item__todos_itens)
        
        if result.empty:
            print("Não existe nenhum item_estoque cadastrado!")
            input("\nPressione Enter para sair do Relatório de Itens ")
            
            return False
        else:
            print("Produtos armazenados: ")
            print(result)
            input("\nPressione Enter para sair do Relatório de Itens ")
            
            return True

    
    def get_item_localizacao_produto_especifico(self):
        id_produto = int(input("Informe o id do produto: "))

        oracle = OracleQueries()
        oracle.connect()
        query_item_localizacao_produto_especifico = f"""
            SELECT distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            FROM produto p
            INNER JOIN item_estoque i
                on i.id_produto = p.id
            where i.id_produto = {id_produto}
            """

        print("\n")

        result = oracle.sqlToDataFrame(query_item_localizacao_produto_especifico)

        if result.empty:
            print(f"O produto({id_produto}) não está em nenhum estoque!")
        else:
            print(result)
        
            
        input("\nPressione Enter para sair do Relatório de Itens ")