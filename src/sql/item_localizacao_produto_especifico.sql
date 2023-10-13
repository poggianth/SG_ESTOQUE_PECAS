select distinct p.id, p.nome, p.descricao, i.estante, i.prateleira
            from produto p
            inner join item_estoque i
                on i.id_produto = p.id
            where i.id_produto = ?
