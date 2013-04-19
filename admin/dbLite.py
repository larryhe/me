import  sqlite3
class Dblite: 
    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.c = conn.cursor()

    def execQuery(self, sql, *params):
        self.c.execute(sql, *params)
        record = self.c.fetchone()
        return record

    def execQueryAll(self, sql, *params):
        self.c.execute(sql, *params)
        record = self.c.fetchall()
        return record

    def execUpdate(self, sql, *params):
        self.c.execute(sql, *params)
        record = c.fetchone()
