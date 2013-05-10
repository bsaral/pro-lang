<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
<title>Baked Bean Display</title>
</head>
<body style="background-color:#ff9966">
<div style = "margin-left: 0.5in;">
	<h1 style = "color: #ff0099;">Baked Bean Values: page</h1>
	<jsp:useBean id="pageBean" class="hmwrk.BakedBean" />
	<jsp:setProperty name="pageBean" property="*" />
	<h3 style = "color: purple;"> İsim: <jsp:getProperty name="pageBean" property="name" /></h3>
	<h3 style = "color: purple;">Soyisim: <jsp:getProperty name="pageBean" property="surname" /></h3><hr>
</div>
</body>
</html>