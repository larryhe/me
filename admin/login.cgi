#!/usr/bin/python
import cgi, cgitb
form = cgi.FieldStorage()
flag = form.getvalue('error_login', 0);
errMsg = """
<div class="alert alert-error">
    <strong>Error!</strong> User name or password is invalid, Please try again.
</div>
"""
if flag == 0:
    errMsg = ""
print """\
Content-Type: text/html\n
<!DOCTYPE html>
<html lang="en">
<head>
<title>Login to manage blogs</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="../bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
<link href="../res/style.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="login_box">
<form class="form-horizontal" action="/admin/manage.cgi" method="post">
    %s
    <div class="control-group">
    <label class="control-label" for="inputEmail">User Name</label>
    <div class="controls">
    <input type="text" id="username" placeholder="username" name="username">
    </div>
    </div>
    <div class="control-group">
    <label class="control-label" for="inputPassword">Password</label>
    <div class="controls">
    <input type="password" id="password" placeholder="Password" name="password">
    </div>
    </div>
        <div class="control-group">
        <div class="controls">
        <button type="submit" class="btn">Login in</button>
        </div>
        </div>
</form>
</div>
  <div class="footer">
      <p>Powered by <a href="https://github.com/larryhe/tinyhttpd">tinyhttpd</a> and <a href="http://nodejs.org/">node.js</a> and <a href="http://www.sqlite.org/">SQLite</a></p>
  </div>
</div>
</html>
""" % (errMsg,)
