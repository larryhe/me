import  sqlite3, datetime
class Dblite: 
    def __init__(self):
        conf = open('config.txt','r')
        url = conf.readline().rstrip()
        self.conn = sqlite3.connect(url)
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
        sql = "update blog set title=?, content=?, tag=?, status=? where id=?"
        self.execUpdate(sql, params)
        return self.getBlogById(params[4])

    def newBlog(self, params):
        insert = "insert into blog values (?, ?, ?, ?, ?, ?)"
        select = "select max(id) from blog"
        record = self.execQuery(select)
        id = 1
        if record != None and record[0] != None:
            id = record[0] + 1
        args = (id, params[0], params[1], params[2], self.today(), params[3])
        self.execUpdate(insert, args)
        return self.getBlogById(id)

    def getBlogById(self, id):
        params = (id,)
        return self.execQuery('select b.id, b.title, t.desc, b.status, b.created_date, b.content from blog b, tag t where b.tag=t.id and b.id=?', params)

    def getBlogRawById(self, id):
        params = (id,)
        return self.execQuery('select id, title, tag, status, content from blog where id=?', params)

    def today(self):
        today = datetime.date.today()
        return today.strftime('%m-%d-%Y')

    def recent_blogs(self):
        sql = 'select id, title from blog where status=2 order by id desc limit 5'
        return self.execQueryAll(sql)

    def article_by_tags(self):
        sql = 'select t.id, t.desc, count(b.id) from tag t left join (select id, tag from blog where status=2) b on t.id=b.tag group by t.id'
        return self.execQueryAll(sql)

    def get_blog_by_tag(self, tag):
        sql="select b.title,b.content,b.created_date, t.desc from blog b, tag t where b.tag = t.id and b.status=2 and b.tag=?"
        params = (tag,)
        return self.execQueryAll(sql, params)

    def all_blogs(self):
        sql="select b.title,b.content,b.created_date, t.desc from blog b, tag t where b.tag = t.id and b.status=2"
        return self.execQueryAll(sql)
