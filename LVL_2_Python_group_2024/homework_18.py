import sqlite3


with sqlite3.connect('') as con:
    cur = con.cursor()

db_name = input("Введіть ім'я бази даних : ")


list_data = [
    (1, "ItSource", 23, "04.10.2018", 1000000),
    (2, "Codewars", 3, "17.01.2019", 20000),
    (3, "ItCraft", 17, "31.12.2017", 340000),
    (4, "SoftVerse", 1, "25.07.2020", 900000),
    (5, "ItLand", 44, "06.06.2016", 3000000),
    (6, None, 22, "11.08.2011", 440000),
    (7, "PostCode", 22, None, 830000),
    (8, "CraftSource", 13, "31.12.2017", 340000),
    (9, "SoftVerse", 1, "25.07.2020", 900000),
    (10, "ItCraft", 17, "31.12.2017", 340000),
]


with sqlite3.connect(db_name) as con:
    cur = con.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS "TableNoConstraints" (
        id INTEGER,
        client_name TEXT,
        credit_code INTEGER,
        issue_date TEXT,
        amount REAL
    )''')


    cur.execute('''CREATE TABLE IF NOT EXISTS "TableUniqueColumn" (
        id INTEGER,
        client_name TEXT UNIQUE,
        credit_code INTEGER,
        issue_date TEXT,
        amount REAL
    )''')


    cur.execute('''CREATE TABLE IF NOT EXISTS "TableNotNullColumn" (
        id INTEGER,
        client_name TEXT,
        credit_code INTEGER NOT NULL,
        issue_date TEXT,
        amount REAL
    )''')


    cur.executemany('''INSERT INTO "TableNoConstraints" VALUES(?,?,?,?,?)''', list_data)


    try:
        cur.executemany('''INSERT INTO "TableUniqueColumn" VALUES(?,?,?,?,?)''', list_data)
    except sqlite3.IntegrityError as e:
        print(f"Помилка вставки у 'TableUniqueColumn': {e}")


    try:
        cur.executemany('''INSERT INTO "TableNotNullColumn" VALUES(?,?,?,?,?)''', list_data)
    except sqlite3.IntegrityError as e:
        print(f"Помилка вставки у 'TableNotNullColumn': {e}")


    con.commit()

print(f"База даних '{db_name}' створена та заповнена.")


