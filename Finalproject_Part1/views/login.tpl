<!DOCTYPE html>
<html>
	<head>
		<title>Pokemon Site</title>
		<link rel="stylesheet" type="text/css" href="/static/css/style.css">
	</head>
	<body>
		<form id="form_id" method="post" action="/blogs">
			<h1>blog login</h1>
			<div class="logincontainer">
				<label>User Name :</label>
				<input type="text" name="username" id="username"/>
				
				<label>Password :</label>
				<input type="password" name="password" id="password"/>
				
				<input type="submit" value="Login"/>
				<span class="validationalert">The username and password are not correct</span>
			</div>
		</form>
	</body>
</html>	