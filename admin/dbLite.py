import  sqlite3, datetime
class Dblite: 
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()

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
        self.conn.commit()

    def updateBlog(self, params):
        insert = "insert into blog values (?, ?, ?, ?, ?, ?)"
        select = "select max(id) from blog"
        record = self.execQuery(select)
        id = 1
        if record != None:
            id = record[0] + 1
        args = (id, params[0], params[1], params[2], self.today(), params[3])
        self.execUpdate(insert, args)
        return self.getBlogById(id)

    def getBlogById(self, id):
        params = (id,)
        return self.execQuery('select * from blog where id=?', params)

    def today(self):
        today = datetime.date.today()
        return today.strftime('%m-%d-%Y')
