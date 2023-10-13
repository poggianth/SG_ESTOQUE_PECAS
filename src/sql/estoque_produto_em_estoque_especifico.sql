select p.*
from item_estoque ie
inner join produto p
on ie.id_produto = p.id and ie.id_estoque = ?