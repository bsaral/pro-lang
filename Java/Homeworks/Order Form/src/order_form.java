package hmwrk;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Stack;
import java.util.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;


@WebServlet("/order_form")
public class order_form extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static final int String = 0;
	private static final int Stack = 0;
	private static final int Arraylist = 0;
       
    public order_form() {
        super();
       
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		HttpSession session = request.getSession();
		
		    Stack liste = (Stack)session.getAttribute("liste");
			if (liste == null){
				liste =  new Stack();
			}
			String eleman = request.getParameter("item");
			if (eleman != null){
				liste.push(eleman);
			}
			session.setAttribute("liste", liste);
			
			out.println("<!DOCTYPE html>\n" +
					"<html>\n" +
					"<head><title>Kaydedilenler</title></head>\n" +
					"<body style = \" margin-top:50px;margin-left: 3.5in\">\n<h1 style = \"color:#6666cc;margin-left: 0in\">Kaydedilenler </h1><br>"+
					"<link href='http://twitter.github.com/bootstrap/assets/css/bootstrap.css' rel='stylesheet'>"+
					"<div class = hero-unit style = width:400px;height:200px>"
					);
			int count = liste.size();
			if (count == 0){
				out.println("listemiz bos");
			}
			else{
				
				for(int i = 0 ; i < count ; i ++){
					out.println("<li>"+liste.get(i)+"</li>");
				}
				
			
		}
	}
}


