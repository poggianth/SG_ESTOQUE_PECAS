from conexion.oracle_queries import OracleQueries

def crate_tables(query_sql: str):
    list_of_commands = query_sql.split(";")

    oracle = OracleQueries()
    oracle.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(f"Running command: {command}")
            try:
                oracle.executeDDL(command)
                print("Successfuly executed")
            except Exception as error:
                print(f"Error while running a command: {error}")

def generate_records(query_sql:str):
    list_of_commands = query_sql.split(";")

    oracle = OracleQueries()
    oracle.connect()

    for command in list_of_commands:
        if len(command) > 0:
            print(f"Running command: {command}")
            try:
                oracle.write(command)
                print("Successfuly executed")
            except Exception as error:
                print(f"Error while running a command: {error}")

def run():
    query_create_tables = """
        CREATE TABLE estoque (id NUMERIC GENERATED ALWAYS AS IDENTITY PRIMARY KEY, tipo VARCHAR(45) NOT NULL);

        CREATE TABLE produto (
        id NUMERIC GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        nome VARCHAR(45) NOT NULL,
        descricao VARCHAR(45) NOT NULL,
        quantidade NUMERIC NOT NULL,
        categoria  VARCHAR(45) NOT NULL,
        preco_unitario NUMERIC(20, 2) NOT NULL,
        quantidade_reposicao NUMERIC(20) NOT NULL);

        CREATE TABLE item_estoque (
        id NUMERIC GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        id_estoque NUMERIC NOT NULL,
        id_produto NUMERIC NOT NULL,
        estante VARCHAR(45) NOT NULL,
        prateleira NUMERIC NOT NULL);


        ALTER TABLE item_estoque ADD CONSTRAINT item_estoque_id_estoque_estoque_id FOREIGN KEY (id_estoque) REFERENCES estoque(id);
        ALTER TABLE item_estoque ADD CONSTRAINT item_estoque_id_produto_produto_id FOREIGN KEY (id_produto) REFERENCES produto(id);
    """

    query_insert_records = """
        INSERT INTO estoque (tipo) VALUES ('Estoque Principal');
        INSERT INTO estoque (tipo) VALUES ('Estoque de Backup');
        INSERT INTO estoque (tipo) VALUES ('Estoque de Excesso');

        INSERT INTO produto (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES ('Produto 1', 'Descrição do Produto 1', 100, 'Categoria A', 10.99, 50);
        INSERT INTO produto (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES ('Produto 2', 'Descrição do Produto 2', 200, 'Categoria B', 15.50, 30);
        INSERT INTO produto (nome, descricao, quantidade, categoria, preco_unitario, quantidade_reposicao) VALUES ('Produto 3', 'Descrição do Produto 3', 150, 'Categoria A', 8.75, 40);
    """

    query_insert_related_records = """
        INSERT INTO item_estoque (id_estoque, id_produto, estante, prateleira) VALUES (1, 1, 'Estante A', 1);
        INSERT INTO item_estoque (id_estoque, id_produto, estante, prateleira) VALUES (1, 2, 'Estante B', 2);
        INSERT INTO item_estoque (id_estoque, id_produto, estante, prateleira) VALUES (2, 2, 'Estante A', 3);
        INSERT INTO item_estoque (id_estoque, id_produto, estante, prateleira) VALUES (3, 3, 'Estante C', 4);
    """

    crate_tables(query_create_tables)
    print("Tables successfully created!")

    generate_records(query_insert_records)
    print("Records successfully generated!")

    generate_records(query_insert_related_records)
    print("Records successfully generated!")

run()