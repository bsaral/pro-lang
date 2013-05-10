<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
<title>Insert title here</title>
</head>
<body style="background-color:#ff9966">
<div style = "margin-left: 0.5in;">
	<h1 style = "color: #6666cc;">BakedBeanDisplay-application</h1>
	<jsp:useBean id="applicationBean" class="hmwrk.BakedBean" scope="session" />
	<jsp:setProperty name="applicationBean" property="*" />
	<h3 style = "color: purple;">İsim: <jsp:getProperty name="applicationBean" property="name" /></h3>
	<h3 style = "color: purple;">Soyisim: <jsp:getProperty name="applicationBean" property="surname" /></h3><hr>
	<jsp:include page="BakedBeanDisplay-session.jsp" />
</div>
</body>
</html>