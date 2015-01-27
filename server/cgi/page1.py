#!/usr/bin/env python

import cgi
 
form = cgi.FieldStorage()

data_string = ""

if "mainhobby" in form and "birthdate" in form:
	data_string = "Your hobby: {0}, and Birthdate: {1}"\
		.format(form["mainhobby"].value,form["birthdate"].value)

print """Content-type: text/html\r\n
\r\n
<html>
<head>
<title>ENTER YOUR INFO</title>
</head>
<body>
<h1>Please fill in form</h1>
<div>{}</div>
<form method="post" action="page2.py">
<label>Name:</label>
<input type="text" name="name" />
</br>
<label>Family:</label>
<input type="text" name="family" />
<br/>
<label>Are you living?</label>
<input type="checkbox" name="living" value="true"/>
<br/>
<input type="submit" value="Submit" />
</form>
</body>
</html>
""".format(data_string)
