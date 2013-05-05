<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
<title>HIZ HESAPLAMA</title>
</head>
<body style="background-color:#ff9966">
<%@ page errorPage="/WEB-INF/error.jsp" %>
<% 
	Float furlongs = Float.parseFloat(request.getParameter("furlongs"));
	Float fortnights =Float.parseFloat(request.getParameter("fortnights"));
	Float speed = furlongs/fortnights;
%>
<div style = "margin-left:-1in;margin-top: 1in">
	<table border=1 align="center" class="table table-bordered" >
		<tr  style = "background-color: #ffff66">
			<th>Parameter Name</th><th>Parameter Value(s)</th>
			<tr ><th>DİSTANCE : <td></b><%= furlongs %> furlongs
			<tr ><th> TİME : <td><%= fortnights %> fortnights
			<tr ><th> SPEED : <td><%= speed %> speed
		</td>
	</tr>

</table>
</div>
</body>
</html>