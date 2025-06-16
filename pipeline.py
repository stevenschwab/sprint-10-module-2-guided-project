'''Data Pipeline for moving sqlite db to postgres hosted db'''

import psycopg2
from dotenv import load_dotenv
import os
import sqlite3
from queries import *

# Load .env file
load_dotenv()

# Get secrets
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")

# connecting to PostgreSQL DB
pg_conn = psycopg2.connect(f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?sslmode=require")

pg_curs = pg_conn.cursor()

# Connecting to SQLite DB

sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# generic execute_query function that can work with either cursor object

def execute_query(curs, query=select_all):
    result = curs.execute(query)
    return result

def populate_pg_character_table(curs, conn, characters_list):
    for character in characters_list:
        insert_statement = """
            INSERT INTO charactercreator_character (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
            VALUES {};
        """.format(character[1:])
        curs.execute(insert_statement)
        conn.commit()

if __name__ == '__main__':
    SL_CHARACTERS = execute_query(sl_curs, get_characters).fetchall()
    print(SL_CHARACTERS[:5])

    execute_query(pg_curs, create_character_table)

    populate_pg_character_table(pg_curs, pg_conn, SL_CHARACTERS)