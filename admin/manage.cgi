#!/usr/bin/python
# Import modules for CGI handling and sqlite module
import cgi, cgitb, sqlite3, md5, pdb
m = md5.new()
conn = sqlite3.connect('/Users/larry/local/sbin/me.db')
c = conn.cursor()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from fields
#pdb.set_trace()
username = form.getvalue('username')
password  = form.getvalue('password')
m.update(password)
user_pass = (username, m.hexdigest())
c.execute('SELECT * FROM user WHERE name=? and password=?', user_pass)
record = c.fetchone()
if record == None:
    print "Location: /admin/login.cgi?error_login=y\r\n\r\n"
else:
    print "Content-type:text/html\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Hello - Second CGI Program</title>"
    print "</head>"
    print "<body>"
    print "<h2>Hello %s %s</h2>" % (username, password)
    print "</body>"
    print "</html>"
