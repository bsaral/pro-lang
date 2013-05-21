package coreservlets;

import java.io.*;
import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;

/** Servlet that reads a customer ID and displays
 *  information on the account balance of the customer
 *  who has that ID.
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, 
 *  Spring, Hibernate/JPA, and Java programming</a>.
 */

@WebServlet("/show-balance")
public class ShowBalance extends HttpServlet {
  @Override
  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
      throws ServletException, IOException {
    String customerId = request.getParameter("customerId");
    CustomerLookupService service = new CustomerSimpleMap();
    Customer customer = service.findCustomer(customerId);  // OK to pass null or empty String to findCustomer
    request.setAttribute("customer", customer);
    String address;
    if (customer == null) {
      request.setAttribute("badId", customerId);
      address = "/WEB-INF/results/unknown-customer.jsp";
    } else if (customer.getBalance() < 0) {
      address = "/WEB-INF/results/negative-balance.jsp";
    } else if (customer.getBalance() < 10000) {
      address = "/WEB-INF/results/normal-balance.jsp";
    } else {
      address = "/WEB-INF/results/high-balance.jsp";
    }
    RequestDispatcher dispatcher =
      request.getRequestDispatcher(address);
    dispatcher.forward(request, response);
  }
}
