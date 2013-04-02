package web;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class show_browser
 */
@WebServlet("/show_browser")
public class show_browser extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Show My Browser</title></head>\n" +
				"<body bgcolor=\"#99cc99\" style = \" margin-top:50px;margin-left: 2in\">\n<h1 style = \"color:#6666cc\">Show My Browser </h1><br>");
		
		String browser = (String)request.getHeader("User-Agent");
		browser = browser.toLowerCase();
		
		if(browser.contains("msie"))
			browser = "Internet Explorer";
		else if(browser.contains("opera"))
			browser = "Opera";
		else if(browser.contains("chrome"))
			browser = "Google Chrome";
		else if(browser.contains("firefox"))
			browser = "Mozilla Firefox";
		else if(browser.contains("safari"))
			browser = "Safari";
		else
			browser = "Bilinmiyor :(";
		
		out.println("<h2 style = \"color:purple\"> Kullandiginiz Browser Türü : "+browser+"</h2>");
		
		
	}

	
}
