#!/usr/bin/python
# Import modules for CGI handling and sqlite module
import cgi, cgitb, md5, pdb
from dbLite import Dblite
m = md5.new()
db= Dblite('/Users/larry/local/sbin/me.db')
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
#pdb.set_trace()
username = form.getvalue('username')
password  = form.getvalue('password')
m.update(password)
user_pass = (username, m.hexdigest())
record=db.execQuery('SELECT * FROM user WHERE name=? and password=?', user_pass)
tags=[];
tags.append('<select name="tag">')
tag_record=db.execQueryAll('select * from tag')
for tag in tag_record:
    tags.append('<option value="'+str(tag[0])+'">'+tag[1]+'</option>')
tags.append('</select>')
select_str=''.join(tags)
if record == None:
    print "Location: /admin/login.cgi?error_login=y\r\n\r\n"
else:
    print """\
    Content-type:text/html\r\n\r\n
    <html lang="en">
    <head>
    <title>management page</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <link href="../res/style.css" rel="stylesheet" type="text/css" />
    <script src="../res/jquery-1.9.1.js"></script>
    <script src="../bootstrap/js/bootstrap.min.js"></script>
    </head>
    <body>
    <div id="list_box">
    <button class="btn" data-toggle="modal" data-target="#myModal">Add New Blog</button>
    <table class="table table-hover">
        <thead>
        <tr>
            <th>#</th>
            <th>Title</th>
            <th>Tag</th>
            <th>Status</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>linux kernel exploration</td>
            <td>linux</td>
            <td>draft</td>
        </tr>
        </tbody>
    </table>
<div id="myModal" class="modal hide fade" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
<div class="modal-header">
<button type="button" class="close" data-dismiss="modal" aria-hidden="true">x</button>
<h3 id="myModalLabel">Modal header</h3>
</div>
<div class="modal-body">
<div class="control-group">
<label class="control-label" for="inputTitle">Title</label>
<div class="controls">
<input type="text" id="inputTitle" placeholder="Title">
</div>
</div>
<div class="control-group">
<label class="control-label" for="inputTag">Tag</label>
<div class="controls">
%s
</div>
</div>
<div class="control-group">
<label class="control-label" for="inputStatus">Status</label>
<div class="controls">
<select name="status">
<option value="1">Draft</option>
<option value="2">Published</option>
<option value="3">Deleted</option>
</select>
</div>
<div class="control-group">
<label class="control-label">Blog</label>
<div class="controls">
<textarea rows="8" id="inputBlog"></textarea>
</div>
</div>
</div>

</div>
<div class="modal-footer">
<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
<button class="btn btn-primary">Save</button>
</div>
</div>
    </div>
    <div class="footer">
        <p>Powered by <a href="https://github.com/larryhe/tinyhttpd">tinyhttpd</a> and <a href="http://nodejs.org/">node.js</a> and <a href="http://www.sqlite.org/">SQLite</a></p>
    </div>
    </div>
    </html>
    """ % (select_str,)
