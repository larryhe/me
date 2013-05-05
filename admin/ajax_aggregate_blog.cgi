#!/usr/bin/python
# Import modules for CGI handling and sqlite module
import cgi, cgitb, pdb
from dbLite import Dblite
db= Dblite()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
ret='<div class="recent_blogs">%s</div><div class="article_by_tags">%s</div>'

def recent_blogs():
    row='<li><a href="/detail.cgi?id=%s">%s</a></li>'
    h = []
    #pdb.set_trace()
    posts = db.recent_blogs()
    for p in posts:
        h.append(row % (p[0], p[1],))
    return ''.join(h)

def article_by_tags():
    row='<li><a href="/blog.cgi?tag=%s">%s (%s)</a></li>'
    h = []
    tags = db.article_by_tags()
    for p in tags:
        h.append(row % (p[0], p[1], p[2],))
    return ''.join(h)

print "Content-type:text/html\r\n\r\n"
print ret % (recent_blogs(), article_by_tags(),)

