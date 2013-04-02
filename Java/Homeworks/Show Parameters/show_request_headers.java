package java_web;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/show_request_headers")
public class show_request_headers extends HttpServlet {
	public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Show Request</title></head>\n" +
				"<body bgcolor=\"#ffffcc\" style = \" margin-top:50px;margin-left: 2in\">\n<h1>REQUESTS </h1><br>");
		out.println("<br><b> request method : </b>" + request.getMethod());
		out.println("<br><b> request url : </b>" + request.getRequestURI());
		out.println("<br><b> request method : </b>" + request.getMethod());
		out.println("<br><b> request protocol : </b>" + request.getProtocol());
		
		out.println("<TABLE BORDER=1 ALIGN=CENTER style = \" margin-top:50px;margin-left: 0in\">\n" +
				"<TR BGCOLOR=\"#FFAD00\">\n" +
				"<TH>Parameter Name<TH>Parameter Value(s)");
				Enumeration<String> hnames = request.getHeaderNames();
				
				while (hnames.hasMoreElements()) {
					String hname = (String) hnames.nextElement();
					
					out.println("<TR><TD>"+hname+"<TD></b>"+request.getHeader(hname));
					
				}	
			
	}
}