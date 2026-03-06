import sqlite3

DB_PATH = "arogya_mitra.db"

def check_columns():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    tables = ["users", "workouts", "nutrition", "health_records"]

    for table in tables:

        print(f"\nColumns in {table}:")

        cursor.execute(f"PRAGMA table_info({table})")
        columns = cursor.fetchall()

        for col in columns:
            print(col)

    conn.close()


if __name__ == "__main__":
    check_columns()