import cx_Oracle
from model.produto import Produto

class controller_produto:


    def recebe_dados_produto():
        produto = Produto()
        
        produto.nome = input("Informe o nome: ")
        produto.descricao = input("Informe a descrição: ")
        produto.quantidade = int(input("Informe a quantidade (número inteiro): "))
        produto.categoria = input("Informe a categoria: ")
        produto.preco_unitario = float(input("Informe o preço unitário (número decimal): "))
        produto.quantidade_reposicao = int(input("Informe a quantidade de reposição (número inteiro): "))

        return produto
    
    def lista_produtos():
        try:
            connection = cx_Oracle.connect("SYSTEM/123456@127.0.0.1:1521/xe")
            cursor = connection.cursor() 
            cursor.execute('select * from produto')

            res = cursor.fetchall()

            cursor.close()  
            connection.close()

            return res

        except Exception as error:
            print(f"[OPS] - Erro ao listar produto: {error}")
    
    def lista_unico_produto(id: int) -> Produto:
        try:
            connection = cx_Oracle.connect("SYSTEM/123456@127.0.0.1:1521/xe")
            cursor = connection.cursor() 

            cursor.prepare('select * from produto where id = :id') 
            cursor.execute(None, {'id': id})

            res = cursor.fetchall()
            
            cursor.close()  
            connection.close()

            return res

        except Exception as error:
            print(f"[OPS] - Erro ao listar produto: {error}")


    # def insere_produto(produto: Produto):
    #     try:
    #         con = cx_Oracle.connect("SYSTEM/123456@127.0.0.1:1521/xe")
    #         cur = con.cursor() 
    #         cur.arraysize = 100 
    #         cur.execute('select * from produto')

    #         res = cur.fetchall() 
    #         print(f"Res: ${res}")
    #         # uncomment to display the query results 
    #         cur.close()  
    #         con.close()

    #     except Exception as error:
    #         print(f"[OPS] - Erro ao inserir produto: {error}")

        # cursor.execute("INSERT INTO PRODUTO (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES (:nome, :descricao, :quantidade, :categoria, :preco_unitario, :quantidade_reposicao);")

    # def seleciona_todos_produto():
    #     oracle = oracle_queries()
    #     cursor = oracle.connect()