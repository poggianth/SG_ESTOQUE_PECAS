from conexion.oracle_queries import OracleQueries
from reports import relatorios
from controller import controller_estoque, controller_produto

control_estoque = controller_estoque.Controller_Estoque()
control_produto = controller_produto.Controller_Produto()
relatorio = relatorios.Relatorio()

class Controller_Item_Estoque:

    def existe_item_estoque(self, oracle: OracleQueries, id_item_estoque: int):
        result = oracle.sqlToDataFrame(f"SELECT id FROM item_estoque where id = {id_item_estoque}")
        return not result.empty
    
    def inserir_item_estoque(self):
        try:
            oracle = OracleQueries()
            cursor = oracle.connect()

            if relatorio.get_produto_todos_produtos():
                id_produto = int(input("Informe o código(id) do produto que deseja armazenar: "))
                if control_produto.existe_produto(oracle, id_produto):
                    if relatorio.get_estoque_todos_estoques():
                        id_estoque = int(input("Informe o código(id) do estoque onde irá armazenar: "))
                        if control_estoque.existe_estoque(oracle, id_estoque):
                            estante = input("Informe a estante onde o produto ficará: ")
                            prateleira = int(input("Informe o número da prateleira: "))

                            cursor.execute(f"""INSERT INTO item_estoque (id_estoque, id_produto, estante, prateleira) VALUES ({id_estoque}, {id_produto}, '{estante}', {prateleira})""")

                            oracle.conn.commit()
                            print("\nProduto armazenado com sucesso!")

                            print("""\nDeseja armazenar mais um produto?
                                    [1] - Sim
                                    [0] - Não""")
                            opcao_novamente = int(input("Informe sua opção: "))
                            
                            if opcao_novamente == 1:
                                self.inserir_item_estoque()
                            
                        else:
                            print(f"[OPS] - Não existe nenhum estoque com o código(id) = {id_estoque}")
                    else:
                        print("Cadastre pelo menos 1 estoque antes de guardar o produto!")
                else:
                    print(f"[OPS] - Não existe nenhum produto com o código = {id_produto}")
            else:
                print("Cadastre pelo menos 1 produto antes de guardá-lo!")
        except Exception as error:
            print(f"[OPS] - Erro ao armazenar produto: {error}")

    def alterar_item_estoque(self):
        # Mostra os itens_armazenados para guiar o usuário
        if relatorio.get_item__todos_itens():
            id_item_estoque = int(input("Informe o código(id) do item_produto que deseja alterar: "))

            try:
                oracle = OracleQueries(can_write=True)
                cursor = oracle.connect()

                if self.existe_item_estoque(oracle, id_item_estoque):
                    if relatorio.get_produto_todos_produtos():
                        id_produto = int(input("Informe o (NOVO) código(id) do produto que deseja armazenar: "))
                        if control_produto.existe_produto(oracle, id_produto):
                            if relatorio.get_estoque_todos_estoques():
                                id_estoque = int(input("Informe o (NOVO) código(id) do estoque onde irá armazenar: "))
                                if control_estoque.existe_estoque(oracle, id_estoque):
                                    estante = input("Informe a (NOVA) estante onde o produto ficará: ")
                                    prateleira = int(input("Informe o (NOVO) número da prateleira: "))

                                    cursor.execute(f"""
                                                   UPDATE item_estoque SET 
                                                    id_estoque = {id_estoque},
                                                    id_produto = {id_produto},
                                                    estante = '{estante}',
                                                    prateleira = {prateleira}
                                                   WHERE id = {id_item_estoque}
                                    """)

                                    oracle.conn.commit()
                                    print("\nLocalização do produto alterada com sucesso!")

                                    print("""\nDeseja alterar a localização de mais um produto?
                                    [1] - Sim
                                    [0] - Não""")
                                    opcao_novamente = int(input("Informe sua opção: "))
                                    
                                    if opcao_novamente == 1:
                                        self.alterar_item_estoque()
                                    
                                else:
                                    print(f"[OPS] - Não existe nenhum estoque com o código(id) = {id_estoque}")
                            else:
                                print("Cadastre pelo menos 1 estoque antes de guardar o produto!")
                        else:
                            print(f"[OPS] - Não existe nenhum produto com o código = {id_produto}")
                    else:
                        print("Cadastre pelo menos 1 produto antes de guardá-lo!")
                else:
                    print(f"Não existe nenhum item_estoque com o código(id) = {id_item_estoque}")

            except Exception as error:
                print(f"[OPS] - Erro ao editar item_estoque: {error}")
    
        else:
            print("Não existe nenhum produto armazenado para ALTERAR! Armazene pelo menos 1")
    
    def excluir_item_estoque(self):
        # Mostra os itens_armazenados para guiar o usuário
        if relatorio.get_item__todos_itens():
            id_item_estoque = int(input("\nInforme o código(id) do item_estoque que irá EXCLUIR: "))

            try:
                oracle = OracleQueries(can_write=True)
                oracle.connect()

                if self.existe_item_estoque(oracle, id_item_estoque):
                    print("""\nTem certeza que deseja excluir o item_estoque selecionado?
                    [1] - Sim
                    [0] - Não""")
                    opcao_certeza = int(input("Informe sua opção: "))
                    
                    if opcao_certeza == 1:
                        oracle.write(f"DELETE FROM item_estoque WHERE id = {id_item_estoque}")

                        oracle.conn.commit()
                        print(f"Item_estoque({id_item_estoque}) excluído com sucesso!")
                    else:
                        print("Operação de exclusão cancelada com sucesso!")
                else:
                    print(f"Não existe nenhum item_estoque com o código = {id_item_estoque}")
            except Exception as error:
                print(f"[OPS] - Erro ao excluir item_estoque: {error}")
            

        else:
            print("Não existe nenhum produto armazenado para ALTERAR! Armazene pelo menos 1")
    

        
    