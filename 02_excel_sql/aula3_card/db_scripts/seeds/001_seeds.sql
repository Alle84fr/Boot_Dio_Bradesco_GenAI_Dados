/*___________________ collections_______________________________________________*/


INSERT INTO tbl_collections (collection_set_name, release_date, total_cards_in_collection)
VALUES 
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62),
('Team Rocket', '2000-04-24', 83);

/*___________________ types_____________________________________________________*/

INSERT INTO tbl_types (type_name)
VALUES 
('Fire'),
('Water'),
('Grass'),
('Electric'),
('Psychic'),
('Fighting'),
('Dark'),
('Steel'),
('Dragon'),
('Fairy');

/*___________________ stages_____________________________________________________*/

INSERT INTO tbl_stages (stage_name)
VALUES 
('Basic'),
('Stage 1'),
('Stage 2');

/*___________________ cards_______________________________________________________*/

-- Example: Charizard from Base Set
INSERT INTO tbl_cards (
    hp, nome, type_id, stage_id, info, attack, dammage, weak, ressis, retreat, card_number_in_collection, collection_id
)
VALUES (
    120, 'Charizard', 1, 3, 'Flame Pokémon', 'Fire Spin', 100, 'Water', 'None', 3, 4, 1
);

-- Example: Pikachu from Jungle
INSERT INTO tbl_cards (
    hp, nome, type_id, stage_id, info, attack, dammage, weak, ressis, retreat, card_number_in_collection, collection_id
)
VALUES (
    40, 'Pikachu', 4, 1, 'Mouse Pokémon', 'Thunder Jolt', 30, 'Fighting', 'Steel', 1, 60, 2
);

-- Example: Gengar from Fossil
INSERT INTO tbl_cards (
    hp, nome, type_id, stage_id, info, attack, dammage, weak, ressis, retreat, card_number_in_collection, collection_id
)
VALUES (
    80, 'Gengar', 5, 3, 'Shadow Pokémon', 'Nightmare', 30, 'Dark', 'Fighting', 1, 5, 3
);

-- Example: Dark Dragonite from Team Rocket
INSERT INTO tbl_cards (
    hp, nome, type_id, stage_id, info, attack, dammage, weak, ressis, retreat, card_number_in_collection, collection_id
)
VALUES (
    120, 'Dark Dragonite', 9, 3, 'Dragon Pokémon', 'Giant Tail', 70, 'Fairy', 'None', 2, 5, 4
);

