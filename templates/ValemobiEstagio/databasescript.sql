CREATE TABLE mercadoria (
	cod 	varchar(50) PRIMARY KEY NOT NULL,
    tip_mer varchar(50) NOT NULL,
    nom 	varchar(50) NOT NULL,
    qtd 	Integer(10) NOT NULL,
    pre 	decimal(10,5) NOT NULL,
    tip_neg varchar(50) NOT NULL,
    dia_hor datetime NOT NULL UNIQUE
)