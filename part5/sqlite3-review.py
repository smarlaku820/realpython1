import sqlite3

with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute('CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)')
    roster_vals = (('Jean-Baptise Zorg', 'Human', 122),
                   ('Korben Dallas', 'Meat Popsicle', 100),
                   ("Ak'not", 'Manglore', -5))
    c.executemany("Insert into Roster values(?,?,?)", roster_vals)
    c.execute("Update Roster set Species='Human' where Name='Korben Dallas'")
    c.execute("Select * from Roster")
    for row in c.fetchall():
        print(row)