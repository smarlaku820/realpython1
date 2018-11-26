import sqlite3

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute('DROP TABLE if exists PEOPLE')
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
    c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")
    connection.commit()
    c.execute("Select * from People")
    for row in c.fetchall():
        print(row)