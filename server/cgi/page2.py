#!/usr/bin/env python

import cgi
 
form = cgi.FieldStorage()

data_string = ""
living_string = ""

if "name" in form and "family" in form:
	data_string = "Hello, {0} {1}".format(form["name"].value,form["family"].value)
else:
	data_string = "No data provided"

if "living" in form and form["living"].value == "true":
	living_string = "We are glad you are alive"
else:
	living_string = "You indicated you are not living. You must be a robot."	

print """Content-type: text/html\r\n
\r\n
<html>
<head>
<title>
{0}
</title>
</head>
<body>
<h1>{0}</h1>
<h4>{1}</h4>
<form method="post" action="page1.py">
<label>Main Hobby:</label>
<input type="text" name="mainhobby" />
</br>
<label>Birthday:</label>
<input type="text" name="birthdate" />
<br/>
<input type="submit" value="Submit" />
</form>
</body>
</html>
""".format(data_string,living_string)
