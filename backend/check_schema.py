import sqlite3

DB_PATH = "arogya_mitra.db"


def check_schema():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("\nDatabase Tables:")

    for table in tables:
        print(table[0])

    conn.close()


if __name__ == "__main__":
    check_schema()