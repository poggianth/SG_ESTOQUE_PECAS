from conexion.oracle_queries import OracleQueries
from reports import relatorios

relatorio = relatorios.Relatorio()


class Controller_Estoque:

    def existe_estoque(self, oracle: OracleQueries, id_estoque: int):
        result = oracle.sqlToDataFrame(f"SELECT id, tipo FROM estoque WHERE id={id_estoque}")
        return not result.empty
    
    def inserir_estoque(self):
        tipo_estoque = input("Informe o tipo: ")

        try:
            oracle = OracleQueries()
            cursor = oracle.connect()

            cursor.execute(
                f"INSERT INTO estoque (tipo) VALUES ('{tipo_estoque}')"
            )

            oracle.conn.commit()
            print("\nEstoque inserido com sucesso!")

        except Exception as error:
            print(f"[OPS] - Erro ao inserir estoque: {error}")

    def alterar_estoque(self):
        # Mostra os estoques cadastrados para guiar o usuário
        relatorio.get_estoque_todos_estoques()

        id_estoque_alterar = int(input("\nInforme o código(id) do estoque que irá ALTERAR: "))

        try:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            if self.existe_estoque(oracle, id_estoque_alterar):
                # Estoque existe
                tipo_estoque_novo = input("Informe o (NOVO) tipo: ")

                oracle.write(f"UPDATE ESTOQUE SET tipo = '{tipo_estoque_novo}' WHERE id = {id_estoque_alterar}")

                oracle.conn.commit()
                print(f"Estoque({id_estoque_alterar}) alterado com sucesso!")
            
            else:
                print(f"Não existe nenhum estoque com o código(id) = {id_estoque_alterar}")

        except Exception as error:

            print(f"[OPS] - Erro ao atualizar estoque: {error}")
    
    def excluir_estoque(self):
        # Mostra os estoques cadastrados para guiar o usuário
        relatorio.get_estoque_todos_estoques()

        id_estoque_excluir = int(input("\nInforme o código(id) do estoque que irá EXCLUIR: "))

        try:
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            if self.existe_estoque(oracle, id_estoque_excluir):
                if self.existe_itens_dependentes(oracle, id_estoque_excluir):
                    self.excluir_itens_dependentes(oracle, id_estoque_excluir)

                    oracle.write(f"DELETE FROM estoque WHERE id={id_estoque_excluir}")

                    print(f"Estoque({id_estoque_excluir}) excluído com sucesso!")
                else:
                    oracle.write(f"DELETE FROM estoque WHERE id={id_estoque_excluir}")
    
                    oracle.conn.commit()
                    print(f"Estoque({id_estoque_excluir}) excluído com sucesso!")
            else:
                print(f"Não existe nenhum estoque com o código(id) = {id_estoque_excluir}")


        except Exception as error:
            print(f"[OPS] - Erro ao excluir estoque: ${error}")

    def existe_itens_dependentes(self, oracle: OracleQueries, id_estoque: int):
        result = oracle.sqlToDataFrame(f"SELECT id FROM item_estoque WHERE id_estoque={id_estoque}")
        
        return not result.empty
    
    def excluir_itens_dependentes(self, oracle: OracleQueries, id_estoque: int):
        try:
            oracle.write(f"DELETE FROM item_estoque WHERE id_estoque = {id_estoque}")
            print(f"Itens dependentes do estoque ({id_estoque}) deletados com sucesso!")
        
        except Exception as error:
            print(f"[OPS] - Erro ao deletar itens dependentes do estoque({id_estoque}): {error}")