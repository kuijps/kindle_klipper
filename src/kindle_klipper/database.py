import pandas as pd
import sqlite3 
import os
from config import HIGHLIGHTS_TABLE


# pass the path to the csv file, the path to the database and the name of the table you want to create
def create_database(file_path, db_path,table_name):

    df = pd.read_csv(file_path)
    conn = sqlite3.connect(db_path)

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # test query
    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print(df)

    conn.close()

def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

def get_random_highlight(conn):
    cursor = conn.execute("SELECT * FROM {HIGHLIGHTS_TABLE} ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()
    

def get_all_highlights(conn):
    cursor = conn.execute("SELECT * FROM {HIGHLIGHTS_TABLE}")
    return cursor.fetchall()
