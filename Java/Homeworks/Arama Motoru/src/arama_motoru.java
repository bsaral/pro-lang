package web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/arama_motoru")
public class arama_motoru extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		String URL = "SearchEngines";
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Arama Motoru</title></head>\n" +
				"<link href='http://twitter.github.com/bootstrap/assets/css/bootstrap.css' rel='stylesheet'>"+
				"<body bgcolor=\"#99cc99\" style = \" margin-top:50px;margin-left: 4.5in\">\n<h1 style = \"color:#6666cc;margin-left: 1in\">Arama Motoru </h1><br>"+
				"<div class = hero-unit style = width:400px;height:200px>"+
				"<FORM ACTION=\"" + URL + "\">\n" + "  <INPUT TYPE=\"TEXT\" NAME=\"searchString\" class=\"input-medium search-query\" style =\"width:2.5in;margin-left: 0.5in\"><P>\n");
		
		Arama_test[] test = Secenekler.getCommonSpecs();
		out.println("<br><br>");
		out.println("<INPUT TYPE=\"submit\" NAME=\"searchEngine\" class=\" btn btn-large btn-danger\" VALUE="+test[0].getnm()+">");
		out.println("<INPUT TYPE=\"submit\" NAME=\"searchEngine\" class=\" btn btn-large btn-warning\" VALUE="+test[1].getnm()+">");
		out.println("<INPUT TYPE=\"submit\" NAME=\"searchEngine\" class=\" btn btn-large btn-success\" VALUE="+test[2].getnm()+">");
		out.println("<INPUT TYPE=\"submit\" NAME=\"searchEngine\" class=\" btn btn-large btn-info\" VALUE="+test[3].getnm()+">");
		
		
	}

}
