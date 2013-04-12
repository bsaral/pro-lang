package hmwrk;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/cookies")
public class cookies extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public cookies() {
        super();
        
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		boolean cookie = true ;
		Cookie[] ck = request.getCookies();
		
		if (ck != null) {
			for(Cookie c: ck){
				if((c.getName().equals("visitor"))&& c.getValue().equals("yes")){
					cookie = false;
					break;
				}
			}
		}
		
		String yaz;
		if (cookie){
			Cookie rvc = new Cookie("visitor", "yes");
			rvc.setMaxAge(60*60*24*365);
			response.addCookie(rvc);
			yaz = "Merhaba Kullanici";
		}
		else
			yaz = "Tekrar Merhaba Ayni Kullanici";
		
		PrintWriter out = response.getWriter();
		request.setCharacterEncoding("UTF-8");
		out.println("<!DOCTYPE html>\n" +
				"<html>\n" +
				"<head><title>Cookies</title></head>\n" +
				"<body style = \" margin-top:50px;margin-left: 3.5in\">\n"+
				"<link href='http://twitter.github.com/bootstrap/assets/css/bootstrap.css' rel='stylesheet'>"+
				"<div class = hero-unit style = width:600px;height:200px;margin-left:1in;margin-top:1in>"+"<h1 style = \"color:#6666cc;\">"+yaz+ "</h1><br>"
				);
		
		
	}

	

}
