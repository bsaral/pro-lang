<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
<title>Request_Parameter_With_Jsp</title>
</head>
<body style="background-color:#ff9966">

<div style = "margin-left:1in;margin-top: 1in">
<TABLE BORDER=1 ALIGN=CENTER class="table table-bordered" >
<TR  style = "background-color: #ffff66">
<TH>Parameter Name</TH><TH>Parameter Value(s)</TH>
<TR ><TH>İSİM<TD></b><%=request.getParameter("isim") %>
<TR ><TH> SOYAD <TD><%= request.getParameter("soyad") %>
<TR><TH> CİNSİYET <TD><%= request.getParameter("check") %>
<TR><TH> MESLEK <TD><%= request.getParameter("meslek") %>
<TR><TH> MESAJ <TD><%= request.getParameter("mesaj") %>
</TD>
</TR>

</TABLE>

</div>
</body>
</html>