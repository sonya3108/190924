import sqlite3


db_path = 'Chinook_Sqlite.sqlite'
with sqlite3.connect(db_path) as con:
    cur = con.cursor()


    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cur.fetchall()]
    print("Таблиці в базі даних:")
    print(tables)

    if 'Customer' in tables:
        cur.execute("SELECT * FROM Customer LIMIT 3;")
        customers = cur.fetchall()
        print("\nПерші 3 записи з таблиці Customer:")
        print(customers)


        cur.execute("SELECT SUM(Total) FROM Invoice;")
        total_sum = cur.fetchone()[0]
        print("\nЗагальна сума елементів поля Total таблиці Invoice:")
        print(total_sum)


        cur.execute("SELECT * FROM Invoice WHERE BillingCity = 'Paris';")
        paris_invoices = cur.fetchall()
        print("\nЗаписи з таблиці Invoice, у яких домашнє місто Paris:")
        print(paris_invoices)


        cur.execute("""
            SELECT * FROM Invoice 
            WHERE InvoiceDate = (SELECT MIN(InvoiceDate) FROM Invoice);
        """)
        oldest_invoice = cur.fetchone()
        print("\nЗапис із найстарішою датою з таблиці Invoice:")
        print(oldest_invoice)


        cur.execute("""
            SELECT * FROM Invoice 
            WHERE InvoiceDate = (SELECT MAX(InvoiceDate) FROM Invoice);
        """)
        newest_invoice = cur.fetchone()
        print("\nЗапис із найсвіжішою датою з таблиці Invoice:")
        print(newest_invoice)
    else:
        print("\nТаблиця Customer відсутня в базі даних!")




















