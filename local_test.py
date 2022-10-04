# test para probar las consultas

import sqlite3
import sys

import pandas as pd


def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur

conn, _ = load_data()
with open("pregunta_06.sql", encoding="utf-8") as file:
    query = file.read()
result = pd.read_sql_query(query, conn).to_dict()

print(result)