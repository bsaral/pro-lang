package java_web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/java_web")

public class java_web extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		PrintWriter out = response.getWriter();
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Kisiler</title></head>\n" +
				"<body style = \" background-color:#ffffcc\">\n" +
				"<div style=\" width: 500px; margin: 150px auto; padding: 10px 30px; border: 1px solid #e1e1e1; background: white;\""+ "</head></body>");
		
		Kisi kisi1 = new Kisi();
		kisi1.set("Betul", "SARAL", 20);
		out.println("<div> Kisi => "+kisi1.get());
		
		Memur memur1 = new Memur();
		memur1.setm(123, "abcd");
		memur1.set("Ercan", "OGUREN", 28);
		out.println("<div> Memur => \n"+memur1.getm()+"\n");
		out.println(memur1.uyur());
		
		Hoca hoca1 = new Hoca();
		hoca1.set("Hayri", "HAYRETETTI", 35);
		out.println("<div> Hoca => \n"+hoca1.get()+"\n");
		out.println(hoca1.sinav());
		
		Ogrenci o2 = new Ogrenci();
		o2.set("Ayse", "fatma", 22);
		o2.setx(3, "bilgisayar muhendisligi", "samsun");
		out.println("<div> Ogrenci => \n"+o2.getx()+"\n");
	}

	
	
}
