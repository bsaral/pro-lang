package hmwrk;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.sun.xml.internal.bind.v2.schemagen.xmlschema.List;


@WebServlet("/OrderPage")
public class OrderPage extends HttpServlet {
public void doGet(HttpServletRequest request,HttpServletResponse response)throws ServletException, IOException {
	
	HttpSession session = request.getSession();
	ShoppingCart cart;
	synchronized(session) {
		cart = (ShoppingCart)session.getAttribute("shoppingCart");

		if (cart == null) {
			cart = new ShoppingCart();
			session.setAttribute("shoppingCart", cart);
		}
		Object itemID;
		if (itemID != null) {
			String numItemsString =
				request.getParameter("numItems");
			if (numItemsString == null) {
				cart.addItem(itemID);
			} else {

				int numItems;
				try {
					numItems = Integer.parseInt(numItemsString);
				} catch(NumberFormatException nfe) {
					numItems = 1;
			}
				cart.setNumOrdered(itemID, numItems);
			}
		}
	}

	response.setContentType("text/html");
	PrintWriter out = response.getWriter();
	String title = "Status of Your Order";
	String docType ="<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " +"Transitional//EN\">\n";
	out.println(docType +"<HTML>\n" +"<HEAD><TITLE>" + title + "</TITLE></HEAD>\n" +"<BODY BGCOLOR=\"#FDF5E6\">\n" +
				"<H1 ALIGN=\"CENTER\">" + title + "</H1>");
	synchronized(session) {
		List itemsOrdered = cart.getItemsOrdered();
		if (((Object) itemsOrdered).size() == 0) {
			out.println("<H2><I>No items in your cart...</I></H2>");
		} else {
			String itemID = request.getParameter("itemID");
			out.println("<TABLE BORDER=1 ALIGN=\"CENTER\">\n" +
					"<TR BGCOLOR=\"#FFAD00\">\n" +
					" <TH>Item ID<TH>Description\n" +
					" <TH>Unit Cost<TH>Number<TH>Total Cost");
			ItemOrder order;

			NumberFormat formatter = NumberFormat.getCurrencyInstance();

			for(int i=0; i<itemsOrdered.size(); i++) {
				order = (ItemOrder)itemsOrdered.get(i);
				out.println ("<TR>\n" +
						" <TD>" + order.getItemID() + "\n" +
						" <TD>" + order.getShortDescription() + "\n" +
						" <TD>" +
						formatter.format(order.getUnitCost()) + "\n" +
						" <TD>" +
						"<FORM>\n" + // Submit to current URL
						"<INPUT TYPE=\"HIDDEN\" NAME=\"itemID\"\n" +
						" VALUE=\"" + order.getItemID() + "\">\n" +
						"<INPUT TYPE=\"TEXT\" NAME=\"numItems\"\n" +
						" SIZE=3 VALUE=\"" +
						order.getNumItems() + "\">\n" +
						"<SMALL>\n" +
						"<INPUT TYPE=\"SUBMIT\"\n "+
						" VALUE=\"Update Order\">\n" +
						"</SMALL>\n" +
						"</FORM>\n" +
						" <TD>" +
						formatter.format(order.getTotalCost()));
						}
						String checkoutURL =
						response.encodeURL("../Checkout.html");

						out.println
							("</TABLE>\n" +
							"<FORM ACTION=\"" + checkoutURL + "\">\n" +
							"<BIG><CENTER>\n" +
							"<INPUT TYPE=\"SUBMIT\"\n" +
							" VALUE=\"Proceed to Checkout\">\n" +
							"</CENTER></BIG></FORM>");
							}
						out.println("</BODY></HTML>");
					}
				}
			}

