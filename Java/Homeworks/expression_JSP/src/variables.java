package hmwrk;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/variables")
public class variables extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setAttribute("isim", "BETÜL");
		request.setAttribute("soyisim", "SARAL");
		RequestDispatcher yol = request.getRequestDispatcher("variables.jsp");
		yol.forward(request, response);
		
	}
}
