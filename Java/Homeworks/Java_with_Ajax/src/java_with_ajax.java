package hmwrk;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/java_with_ajax")
public class java_with_ajax extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public java_with_ajax() {
        super();
       
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		 response.setContentType("text/html");  
		 PrintWriter out = response.getWriter();
		 out.println("<!DOCTYPE html>\n" +
					"<html>\n" +
					"<head><title>Cookies</title></head>\n" +
					"<body style = \" margin-top:50px;margin-left: 3.5in\">\n"+
					"<link href='http://twitter.github.com/bootstrap/assets/css/bootstrap.css' rel='stylesheet'>"+
					"<script type='javascript/text' src='ajax.js'></script>"+
					"<div class = hero-unit style = width:400px;height:200px>"+
					"<div>AJAX ile merhaba</div>  "+
					"<input type = 'button' value ='Sayfayi yenile ' style ='background-color:red;' onclick='javascript:getNewContent();'>"
					);
	}

}
