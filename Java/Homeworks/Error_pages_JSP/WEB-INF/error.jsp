<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
<title>HATA SAYFASI</title>
</head>
<body style="background-color:#ff9966">
<%@ page isErrorPage="true" %>

<div style = "margin-left:2in;margin-top: 0.5in; width:10in;">
	<table border=1 align="center" class="table table-bordered" >
	<tr><th> HIZ HESAPLAMA HATASI </table>
	<h3> ComputeSpeed.jsp reported the following error:
    <I><%= exception %></I>. This problem occurred in the following place:
    <PRE>
<%@ page import="java.io.*" %>
<% exception.printStackTrace(new PrintWriter(out)); %>
</PRE>

</body>
</html>