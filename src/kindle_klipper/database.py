import pandas as pd
import sqlite3 


def update_database(file_path, db_path,table_name):

    df = pd.read_csv(file_path)

    conn = sqlite3.connect(db_path)

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # test query
    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print(df)

    conn.close()

def get_random_highlight(conn):
    cursor = conn.execute("SELECT * FROM highlights ORDER BY RANDOM() LIMIT 1")
    return cursor.fetchone()