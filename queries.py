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