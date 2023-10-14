from conexion.oracle_queries import OracleQueries
from model.produto import Produto
from reports import relatorios

relatorio_produto = relatorios.Relatorio()


class Controller_Produto:

    def recebe_dados_produto(self):
        produto = Produto()

        produto.nome = input("Informe o nome: ")
        produto.descricao = input("Informe a descrição: ")
        produto.quantidade = int(
            input("Informe a quantidade (número inteiro): "))
        produto.categoria = input("Informe a categoria: ")
        produto.preco_unitario = float(
            input("Informe o preço unitário (número decimal): "))
        produto.quantidade_reposicao = int(
            input("Informe a quantidade de reposição (número inteiro): "))

        return produto

    def existe_produto(self, oracle: OracleQueries, id_produto: int):
        result = oracle.sqlToDataFrame(
            f"select id, nome from produto where id={id_produto}")
        return not result.empty

    def inserir_produto(self) -> bool:
        # produto = self.recebe_dados_produto()

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

        except Exception as error:
            print(f"Erro ao inserir produto: {error}")

    def alterar_produto(self):
        # Mostra os produtos cadastrados para guiar o usuário
        relatorio_produto.get_produto_todos_produtos()

        id_produto = int(
            input("\nInforme o código(id) do produto que irá ALTERAR: "))

        try:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            if self.existe_produto(oracle, id_produto):
                # Produto existe
                nome = input("Informe o nome: ")
                descricao = input("Informe a descrição: ")
                quantidade = int(
                    input("Informe a quantidade (número inteiro): "))
                categoria = input("Informe a categoria: ")
                preco_unitario = float(
                    input("Informe o preço unitário (número decimal): "))
                quantidade_reposicao = int(
                    input("Informe a quantidade de reposição (número inteiro): "))

                oracle.write(
                    f"""
                        UPDATE PRODUTO SET nome = '{nome}', descricao = '{descricao}', quantidade = {quantidade}, categoria = '{categoria}', preco_unitario = {preco_unitario}, quantidade_reposicao = {quantidade_reposicao} WHERE id = {id_produto}
                    """
                )

                print("Produto alterado com sucesso!")

            else:
                print(f"Não existe nenhum produto com o código(id): {
                      id_produto}")

        except Exception as error:
            print(f"Erro ao atualizar produto: {error}")

    def excluir_produto(self):
        # Mostra os produtos cadastrados para guiar o usuário
        relatorio_produto.get_produto_todos_produtos()

        id_produto = int(
            input("\nInforme o código(id) do produto que irá EXCLUIR: "))

        try:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            if self.existe_produto(oracle, id_produto):
                oracle.write(f"DELETE FROM produto WHERE id = {id_produto}")

                print("Produto EXCLUÍDO com sucesso!")

            else:
                print(f"Não existe nenhum produto com o código(id): {id_produto}")

        except Exception as error:
            print(f"Erro ao excluir produto: {error}")
