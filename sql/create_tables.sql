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
