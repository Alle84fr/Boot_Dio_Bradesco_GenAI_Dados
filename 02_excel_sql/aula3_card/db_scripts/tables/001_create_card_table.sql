CREATE TABLE tbl_collections (
    id INT IDENTITY(1,1) PRIMARY KEY,
    collection_set_name VARCHAR(100) NOT NULL,
    release_date DATE NOT NULL,
    total_cards_in_collection SMALLINT NOT NULL
);

CREATE TABLE tbl_types (
    id INT IDENTITY(1,1) PRIMARY KEY,
    type_name VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE tbl_stages (
    id INT IDENTITY(1,1) PRIMARY KEY,
    stage_name VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE tbl_cards (
    id INT IDENTITY(1,1) PRIMARY KEY,
    hp SMALLINT,
    nome VARCHAR(80) NOT NULL,
    type_id INT NOT NULL,
    stage_id INT NOT NULL,
    info NVARCHAR(MAX),
    attack VARCHAR(100),
    dammage SMALLINT,
    weak VARCHAR(30),
    ressis VARCHAR(30),
    retreat SMALLINT,
    card_number_in_collection SMALLINT NOT NULL,
    collection_id INT NOT NULL,
    CONSTRAINT fk_collection FOREIGN KEY (collection_id) REFERENCES tbl_collections (id) ON DELETE CASCADE,
    CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES tbl_types (id),
    CONSTRAINT fk_stage FOREIGN KEY (stage_id) REFERENCES tbl_stages (id)
);
