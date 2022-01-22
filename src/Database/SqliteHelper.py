import sqlite3

class SqliteHelper:

    def __init__(self, connectionstring):
        self.connection = sqlite3.connect(connectionstring)
        self.cursor = self.connection.cursor()

    def CreateCarsTable(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Cars (
        model text,
        title text,
        year text,
        kilometer text,
        color text,
        price text,
        date text,
        location text,
        url text
                )
        """)
        self.connection.commit()

    def CheckIfCarExistsByUrl(self, url):
        return len(self.cursor.execute('SELECT * FROM Cars WHERE url = ?', (url,)).fetchone()) > 0

    def InsertCarIfNotExists(self, model:str, title:str, year:str, kilometer:str, color, price:str, date:str, location:str, url:str):
        if self.CheckIfCarExistsByUrl(url):
            print(f"{url} car already exists in the database.")
            return
        self.cursor.execute('INSERT INTO Cars Values (?, ?, ?, ?, ?, ?, ?, ?, ?)', (model, title, year, kilometer, color, price, date, location, url))
        self.connection.commit()