package coreservlets;  

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

/**  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *   coreservlets.com tutorials on servlets, JSP, Struts, JSF 2.0, Ajax, GWT, and Java</a>.
 */

@WebServlet("/find-prime")
public class PrimeServlet extends HttpServlet {
  @Override
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
      throws ServletException, IOException {
    String length = request.getParameter("primeLength");
    ServletContext context = getServletContext();
    synchronized(this) {
      if ((context.getAttribute("primeBean") == null) ||
          (!isMissing(length))) {
        PrimeBean primeBean = new PrimeBean(length);
        context.setAttribute("primeBean", primeBean);
      }
      String address = "/WEB-INF/results/show-prime.jsp";
      RequestDispatcher dispatcher =
        request.getRequestDispatcher(address);
      dispatcher.forward(request, response);
    }
  }
  
  private boolean isMissing(String primeLength) {
    return((primeLength == null) || 
           (primeLength.trim().equals("")));
  }
}
