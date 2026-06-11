import sqlite3

# 1. Connect (creates 'example.db' if it doesn't exist)
with sqlite3.connect("example.db") as connection:
    # 2. Create a cursor to interact with the DB
    cursor = connection.cursor()

    # 3. Create a table
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users
                   (
                       id INTEGER
                       PRIMARY KEY,
                       name TEXT NOT NULL,
                       age INTEGER
                   )
                   ''')

    # 4. Insert data (using ? to prevent SQL injection)
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))

    # 5. Save changes (commit happens automatically with the 'with' block)
    # connection.commit()

# 6. Query data
with sqlite3.connect("example.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
