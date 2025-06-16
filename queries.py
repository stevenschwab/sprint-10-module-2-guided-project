'''Queries for sqlite to Postgres pipeline'''

create_table = """
    CREATE TABLE test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(40) NOT NULL,
        number INT
    );
"""

insert_data = """
    INSERT INTO test_table (name, number)
    VALUES ('A row name', 6), ('Another row', 72);
"""

select_all = """SELECT * FROM test_table;"""

# sqlite queries
row_count = """
    SELECT COUNT(*)
    FROM charactercreator_character;
"""

get_characters = """
    SELECT * FROM charactercreator_character;
"""

get_character_table_info = """
    PRAGMA table.info(charactercreator_character);
"""

create_character_table = """
    CREATE TABLE IF NOT EXISTS charactercreator_character(
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
    );
"""