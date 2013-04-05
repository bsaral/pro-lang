package web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/encoding")
public class encoding extends HttpServlet {
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out;
		if (GzipUtilities.isGzipSupported(request) && !GzipUtilities.isGzipDisabled(request)) {
			out = GzipUtilities.getGzipWriter(response);
			response.setHeader("Content-Encoding", "gzip");
		} 
		else {
			out = response.getWriter();
		}
		
		out.println("<HTML>\n" + "<HEAD><TITLE></TITLE></HEAD>\n" +
		"<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=\"CENTER\">Encoding Denemesi</H1>\n");
		
		String line = "bsaral ";
		for(int i=0; i<100; i++) {
		out.println(line);
		}
		out.println("</BODY></HTML>");
		out.close();
		
	}
}

	


