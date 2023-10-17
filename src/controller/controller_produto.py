from conexion.oracle_queries import OracleQueries
from reports import relatorios

relatorio = relatorios.Relatorio()


class Controller_Produto:

    def existe_produto(self, oracle: OracleQueries, id_produto: int):
        result = oracle.sqlToDataFrame(
            f"SELECT id, nome FROM produto WHERE id={id_produto}")
        return not result.empty

    def inserir_produto(self):

        novo_produto = {
            'nome': input("Informe o nome: "),
            'descricao': input("Informe a descrição: "),
            'quantidade': int(input("Informe a quantidade (número inteiro): ")),
            'categoria': input("Informe a categoria: "),
            'preco_unitario': float(input("Informe o preço unitário (número decimal): ")),
            'quantidade_reposicao': int(input("Informe a quantidade de reposição (número inteiro): "))
        }

        try:
            oracle = OracleQueries()
            cursor = oracle.connect()

            cursor.execute(
                """
                INSERT INTO produto (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES (:nome, :descricao, :quantidade, :categoria, :preco_unitario, :quantidade_reposicao)
                """, novo_produto
            )

            oracle.conn.commit()
            print("\nProduto inserido com sucesso!")

            print("""\nDeseja inserir um novo produto?
              [1] - Sim
              [0] - Não""")
            opcao_novamente = int(input("Informe sua opção: "))
            
            if opcao_novamente == 1:
                self.inserir_produto()

        except Exception as error:
            print(f"[OPS] - Erro ao inserir produto: {error}")

    def alterar_produto(self):
        # Mostra os produtos cadastrados para guiar o usuário
        if relatorio.get_produto_todos_produtos():

            id_produto_alterar = int(
                input("\nInforme o código(id) do produto que irá ALTERAR: "))

            try:
                oracle = OracleQueries(can_write=True)
                oracle.connect()

                if self.existe_produto(oracle, id_produto_alterar):
                    # Produto existe
                    nome = input("Informe o (NOVO) nome: ")
                    descricao = input("Informe a (NOVA) descrição: ")
                    quantidade = int(
                        input("Informe a (NOVA) quantidade (número inteiro): "))
                    categoria = input("Informe a (NOVA) categoria: ")
                    preco_unitario = float(
                        input("Informe o (NOVO) preço unitário (número decimal): "))
                    quantidade_reposicao = int(
                        input("Informe a (NOVA) quantidade de reposição (número inteiro): "))

                    oracle.write(
                        f"""
                            UPDATE PRODUTO SET nome = '{nome}', descricao = '{descricao}', quantidade = {quantidade}, categoria = '{categoria}', preco_unitario = {preco_unitario}, quantidade_reposicao = {quantidade_reposicao} WHERE id = {id_produto_alterar}
                        """
                    )

                    oracle.conn.commit()
                    print(f"Produto({id_produto_alterar}) alterado com sucesso!")

                    print("""\nDeseja alterar mais um produto?
                    [1] - Sim
                    [0] - Não""")
                    opcao_novamente = int(input("Informe sua opção: "))
                    
                    if opcao_novamente == 1:
                        self.alterar_produto()

                else:
                    print(f"Não existe nenhum produto com o código(id): {id_produto_alterar}")
                

            except Exception as error:
                print(f"[OPS] - Erro ao atualizar produto: {error}")
        
        else:
            print("Não existe nenhum produto cadastrado para ALTERAR! Cadastre pelo menos 1")

    def excluir_produto(self):
        # Mostra os produtos cadastrados para guiar o usuário
        if relatorio.get_produto_todos_produtos():

            id_produto_excluir = int(
                input("\nInforme o código(id) do produto que irá EXCLUIR: "))
            
            try:
                oracle = OracleQueries(can_write=True)
                oracle.connect()

                if self.existe_produto(oracle, id_produto_excluir):
                    print("""\nTem certeza que deseja excluir o produto selecionado?
                    [1] - Sim
                    [0] - Não""")
                    opcao_certeza = int(input("Informe sua opção: "))
                    
                    if opcao_certeza == 1:
                        if self.existe_itens_dependentes(oracle, id_produto_excluir):
                            self.excluir_itens_dependentes(oracle, id_produto_excluir)
                            
                            oracle.write(f"DELETE FROM produto WHERE id = {id_produto_excluir}")
                            
                            oracle.conn.commit()
                            print(f"Produto({id_produto_excluir}) excluído com sucesso!")
                        else:
                            oracle.write(f"DELETE FROM produto WHERE id = {id_produto_excluir}")
                            
                            print(f"Produto({id_produto_excluir}) excluído com sucesso!")
                    else:
                        print("Operação de exclusão cancelada com sucesso!")
                else:
                    print(f"Não existe nenhum produto com o código(id): {id_produto_excluir}")

            except Exception as error:
                print(f"[OPS] - Erro ao excluir produto: {error}")
            
        else:
            print("Não existe nenhum produto cadastrado para EXCLUIR! Cadastre pelo menos 1")
    

    def existe_itens_dependentes(self, oracle: OracleQueries, id_produto: int):
        result = oracle.sqlToDataFrame(f"SELECT id FROM item_estoque WHERE id_produto={id_produto}")
        
        return not result.empty
    

    def excluir_itens_dependentes(self, oracle: OracleQueries, id_produto: int):
        try:
            oracle.write(f"DELETE FROM item_estoque WHERE id_produto = {id_produto}")
            print(f"Itens dependentes do produto ({id_produto}) deletados com sucesso!")

        except Exception as error:
            print(f"[OPS] - Erro ao deletar itens dependentes do produto({id_produto}): {error}")
