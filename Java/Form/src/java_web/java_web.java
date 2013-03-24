package java_web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class java_web
 */
@WebServlet("/java_web")
public class java_web extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Deneme Sayfasi</title></head>\n" +
				"<body bgcolor=\"#ffffcc\" style = \" margin-top:50px;margin-left: 5in;\">\n" +
				"<h1>KIMLIK </h1>\n" +"<ul>\n"+"<li><b> AD => </b>"+request.getParameter("isim") + "\n"+
				"<li><b> SOYAD => </b>"+request.getParameter("soyad") + "\n"+
				"<li><b> MESAJ => </b>"+request.getParameter("meslek") + "\n"+
				"<li><b> AD => </b>"+request.getParameter("mesaj") + "\n"+
				"</body></html>");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
