import cx_Oracle
from model.produto import Produto

# def conectar_banco(script_sql):
#     try:
#         # Estabeleça a conexão com o banco de dados
#         connection = cx_Oracle.connect("SYSTEM/123456@localhost:1521/xe")

#         # Crie um cursor
#         cursor = connection.cursor()

#         # Execute o script SQL fornecido como parâmetro
#         cursor.execute(script_sql)

#     except cx_Oracle.Error as error:
#         print(f"Erro ao conectar ao banco de dados: {error}")

#     finally:
#         # Feche o cursor e a conexão, independentemente do resultado
#         if 'cursor' in locals():
#             cursor.close()
#         if 'connection' in locals():
#             connection.close()


def executa_sql(produto: Produto):
    try:
        # Estabeleça a conexão com o banco de dados
        connection = cx_Oracle.connect("SYSTEM/123456@127.0.0.1:1521/xe")

        # Crie um cursor
        cursor = connection.cursor()

        # Script SQL com placeholders para os parâmetros
        sql_inserir_produto = ("begin INSERT INTO sua_tabela (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES ({produto.get_nome}, {produto.get_descricao}, {produto.get_quantidade}, {produto.get_categoria}, {produto.get_preco_unitario}, {produto.get_quantidade_reposicao});")

        # Execute o SQL com os parâmetros do objeto produto
        cursor.execute(sql_inserir_produto, produto)

        # Confirme a transação
        connection.commit()

        # # Obtenha o ID da linha inserida
        # id_inserido = cursor.lastrowid

        # return id_inserido

    except cx_Oracle.Error as error:
        print(f"Erro ao inserir produto: {error}")
        return -1

    finally:
        # Feche o cursor e a conexão, independentemente do resultado
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
