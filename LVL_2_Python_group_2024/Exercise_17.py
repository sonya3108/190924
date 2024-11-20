import sqlite3

#Основні типи файлів для SQLite DB
#.db
#.db3
#.sqlite
#.sqlite3

# sql_connect = sqlite3.connect('C:/Users/Administrator/Downloads/test_1_1.db')
# cur = sql_connect.cursor() #об'єкт курсора, який необхідний для взаємодії з об'єктами бд
# sql_connect.close()


# with sqlite3.connect('test_1_1.db') as con:
#     cur = con.cursor()
#
#     cur.execute('''CREATE TABLE "Account" (
#     UserId INTEGER,
#     Login TEXT NOT NULL UNIQUE,
#     Password TEXT NOT NULL,
#     Email TEXT,
#     PRIMARY KEY("UserId" AUTOINCREMENT)
#     )''')
#
#     cur.execute('''INSERT INTO "Account" VALUES(
#     NULL,
#     "taras123",
#     "1q2w3e4r5t6y",
#     "tarik77@gmail.com"
#     )''')
#
#     list_1 =  [
#         ( None, "tar123",   "1q2w3e4r5t6y",     "tarik77@gmail.com" ),
#         (None, "vasyl5436", "1q2w3e4r5t6y", "vassa@gmail.com"),
#         (None, "daniil", "1q2w3e4r5t6y", "dan111@gmail.com"),
#         (None, "inor", "32er23r43", "inor123@gmail.com"),
#         ]
#
#     cur.executemany(f'''INSERT INTO "Account" VALUES(?,?,?,?)''', list_1)
#
#
#     con.commit()