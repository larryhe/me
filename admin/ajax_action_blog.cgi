#!/usr/bin/python
# Import modules for CGI handling and sqlite module
import cgi, cgitb, pdb
from dbLite import Dblite
db= Dblite('/Users/larry/local/sbin/me.db')
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
action = form.getvalue('action','new')
select_body_tag="<select>%s</select><table>%s</table>"
ret=''

def blog_row(blog):
    body_tag='<tr rowid="%s"><td>%s</td><td><a href="#">%s</a></td><td>%s</td><td>%s</td></tr>'
    return body_tag % (blog[0],blog[0], blog[1], blog[2], convert_status(blog[3]),)

def update_blog(form):
    params = (form.getvalue('title','title'), form.getvalue('content','content'), form.getvalue('tag',1), form.getvalue('status',1))
    #pdb.set_trace()
    blog = db.updateBlog(params)
    return blog_row(blog)

def get_form(blog):
    form='<div class="title">%s</div><div class="tag">%s</div><div class="status">%s</div><div class="content">%s</div>'
    print form % (blog[0], blog[1], blog[2], blog[3], )

def convert_status(status):
    if status == 1:
        return "Drafted"
    elif status == 2:
        return "Published"
    else:
        return "Deleted"
    
if action == 'config':
    #build tag list html
    tags=db.execQueryAll('select * from tag')
    blogs=db.execQueryAll('select * from blog')
    options=[]
    rows=[]
    for tag in tags:
        options.append('<option value="%s">%s</option>' % (tag[0], tag[1],))
    for blog in blogs:
        rows.append(blog_row(blog))
    ret = select_body_tag % (''.join(options), ''.join(rows), )
elif action == 'new' or action == 'del' or action == 'update':
    ret = update_blog(form)
else:
    id = form.getvalue("id")
    blog = db.getBlogById(id)
    ret = get_form(blog)
print "Content-type:text/html\r\n\r\n"
print ret 

