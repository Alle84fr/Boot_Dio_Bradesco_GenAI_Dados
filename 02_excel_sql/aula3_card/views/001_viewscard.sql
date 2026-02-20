CREATE VIEW vw_cards_detalhado AS
SELECT 
    c.id,
    c.hp,
    c.nome,
    t.type_name AS tipo,
    s.stage_name AS estagio,
    c.info,
    c.attack,
    c.dammage,
    c.weak,
    c.ressis,
    c.retreat,
    c.card_number_in_collection,
    col.collection_set_name AS colecao,
    col.release_date AS data_lancamento,
    col.total_cards_in_collection AS total_cartas_colecao
FROM tbl_cards c
INNER JOIN tbl_types t ON c.type_id = t.id
INNER JOIN tbl_stages s ON c.stage_id = s.id
INNER JOIN tbl_collections col ON c.collection_id = col.id;

/*Aqui ele faz um join*/

/* 
Para ver ou chama :*/

SELECT * FROM vw_cards_detalhado

/* OU
select chamando coluna por coluna
mesma coisa só que chamando de outra forma*/

SELECT id, hp, nome, tipo, estagio, info, attack, dammage, weak, ressis, retreat, card_number_in_collection, colecao, data_lancamento, total_cartas_colecao 
FROM vw_cards_detalhado;

