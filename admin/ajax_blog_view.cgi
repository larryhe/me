#!/usr/bin/python
# Import modules for CGI handling and sqlite module
import cgi, cgitb, pdb
from dbLite import Dblite
db= Dblite()
# Create instance of FieldStorage 
# Get data from fields
article="""
    <div class="article">
        <h3>%s</h3>
        <p class="content">%s</p>
        <span class="info"><i>Posted on</i> <b>%s</b> <i>Tagged under</i> <b>%s</b></span>
    </div>"""

def blog_by_id(id):
    h = []
    #pdb.set_trace()
    blog = db.getBlogById(id)
    return article % (blog[1], blog[5], blog[4], blog[2], )

def blog_by_tag(tag):
    h = []
    tags = db.get_blog_by_tag(tag)
    for p in tags:
        h.append(article % (p[0], p[1], p[2], p[3], ))
    return ''.join(h)

def all_blogs():
    h = []
    tags = db.all_blogs()
    for p in tags:
        h.append(article % (p[0], p[1], p[2], p[3], ))
    return ''.join(h)

form = cgi.FieldStorage() 
ret = ''
id = form.getvalue('id', None)
tag = form.getvalue('tag',None)
if id != None:
    ret = blog_by_id(id)
elif tag != None:
    ret = blog_by_tag(form.getvalue('tag'))
else:
    ret = all_blogs()
print "Content-type:text/html\r\n\r\n"
print ret 

