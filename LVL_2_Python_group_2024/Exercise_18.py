import sqlite3

with sqlite3.connect('Chinook_Sqlite.sqlite') as con:
    cur = con.cursor()
    """#DDL(data definition language) - запити для керування об'єктами БД(таблиці, представлення(views), індекси, триггери)"""
    #CREATE - оператор для створення об'єкта БД
    #       CREATE TABLE "Account" (
        #       UserId INTEGER,
        #       Login TEXT NOT NULL UNIQUE,
        #       Password TEXT NOT NULL,
        #       Email TEXT,
        #       PRIMARY KEY("UserId" AUTOINCREMENT)
        #       )

    #ALTER - оператор для редагування об'єктів БД
        # ALTER TABLE "Account" RENAME TO "FaceBook"

        # ALTER TABLE "Account" ADD COLUMN "PhoneNumber" TEXT UNIQUE

    #DROP - оператор видалення об'єктів бд
        #DROP TABLE "Account"



    '''DML (data manipulation language) - запити для керування (маніпуляцією) даними'''
    #CRUID
    # CR - Create
    # U - Update
    # I - Insert
    # D - Delete

    #UPDATE - оператор оновлення, модифікації вже існуючих в таблиці даних
    #МАСОВИЙ ЗАПИТ який замінить всі стовпчики
        # UPDATE Artist
        #         SET Artist.Name #Як приклад коли таблиця в запиті не одна
        #         SET Name = 'Abracadabra'

    # Запит до конкретного елементу
        # UPDATE Artist
        #         SET Name = 'Abracadabra'
        #         WHERE ArtistId == 310

    # cur.execute("""UPDATE Artist
    #             SET Name = 'Abracadabra'
    #             WHERE ArtistId == 310""")

    #INSERT - оператор запису даних в таблицю
        #INSERT INTO Artist VALUES(NULL, "Bringht Me The Horizon")
    # cur.execute('''INSERT INTO Artist VALUES(NULL, "Bringht Me The Horizon")''')

    #DELETE - оператор видалення записів з таблиці
        #DELETE FROM Artist
        #   WHERE ArtistId == 308
    # cur.execute(''' DELETE FROM Artist
    #                     WHERE ArtistId == 308''')
    #
    # cur.execute(''' DELETE FROM Artist
    #                         WHERE ArtistId > 300''')


    #SELECT - оператор для пошуку даних в таблицях
        #SELECT ArtistId FROM Artist
    # cur.execute('''SELECT ArtistId, Name FROM Artist''')
    # cur.execute('''SELECT Name, ArtistId, Name  FROM Artist''')
    # cur.execute('''SELECT *  FROM Customer''')

    #МЕТОДИ для перегляду результатів запиту
    #cur.fetchone() #- отримання однгого рядка даних після запиту
    # cur.fetchmany(count) - яку кількість рядків даних отримаємо після запиту
    # cur.fetchall() - отримання всього що знайшов запит


    #LIMIT - оператор для зазначення кількості шукаємих рядків даних в таблиці
    # cur.execute('''SELECT ArtistId, Name FROM Artist LIMIT 5''')

    #WHERE - умовний оператор для запитів
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                     WHERE ArtistId % 2 == 0''')

    # AND OR
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                         WHERE ArtistId % 2 == 0 AND Name == "GodGoury"''')

    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                            WHERE ArtistId % 2 == 0 OR Name == "GodGoury"''')

    #IN - пошук одного серед багатьох
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                WHERE Name == "AC/DC" OR Name == "Accept" OR Name == "Thre Days Grace"''')

    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                   WHERE Name IN ("AC/DC","Accept","Thre Days Grace")''')

    #LIKE - оператор для пошуку за шаблонами (майже регулярні вирази)
    # %  - будь яка кількість символів або зовсім їх відсутність
    # _  - один будь який символ

    #Знайти всі рокбенди назва яких починається з літери "а"
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                       WHERE Name LIKE "a%" ''')

    # Знайти всі рокбенди назва яких починається з літери "а" та окрім неї в назві ще присутньо 4и літери
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                          WHERE Name LIKE "a____" ''')

    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                             WHERE Name LIKE "aa%" ''')

    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                                 WHERE Name LIKE "%aa%" ''')
    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                                    WHERE Name LIKE "%_aa%" ''')

    # cur.execute('''SELECT ArtistId, Name FROM Artist
    #                                                       WHERE Name LIKE "___ ______" ''')

    print(cur.fetchall())

    con.commit()

