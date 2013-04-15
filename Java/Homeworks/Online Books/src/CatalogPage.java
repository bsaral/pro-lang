package hmwrk;

import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public abstract class CatalogPage extends HttpServlet {
	private CatalogItem[] items;
	private String[] itemIDs;
	private String title;

protected void setItems(String[] itemIDs) {
	this.itemIDs = itemIDs;
	items = new CatalogItem[itemIDs.length];
	for(int i=0; i<items.length; i++) {
		items[i] = Catalog.getItem(itemIDs[i]);
	}
}

protected void setTitle(String title) {
	this.title = title;
}

public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	if (items == null) {
		response.sendError(response.SC_NOT_FOUND,"Missing Items.");
		return;
	}
	response.setContentType("text/html");
	PrintWriter out = response.getWriter();
	out.println("<HTML>\n" +"<HEAD><TITLE>" + title + "</TITLE></HEAD>\n" + "<BODY BGCOLOR=\"#FDF5E6\">\n" +"<H1 ALIGN=\"CENTER\">" + title + "</H1>");
	
	CatalogItem item;
	for(int i=0; i<items.length; i++) {
		out.println("<HR>");
		item = items[i];
	
		if (item == null) {
			out.println("<FONT COLOR=\"RED\">" +"Unknown item ID " + itemIDs[i] +"</FONT>");
		} 
		else {
			out.println();
			String formURL = "/servlet/coreservlets.OrderPage";
	
			formURL = response.encodeURL(formURL);
			out.println("<FORM ACTION=\"" + formURL + "\">\n" + "<INPUT TYPE=\"HIDDEN\" NAME=\"itemID\" " +" VALUE=\"" + item.getItemID() + "\">\n" +
						"<H2>" + item.getShortDescription() +" ($" + item.getCost() + ")</H2>\n" + item.getLongDescription() + "\n" +
						"<P>\n<CENTER>\n" + "<INPUT TYPE=\"SUBMIT\" " + "VALUE=\"Add to Shopping Cart\">\n" +"</CENTER>\n<P>\n</FORM>");
			}
		}
	out.println("<HR>\n</BODY></HTML>");
	}
}
			
			
			
			
			
			
			
			
			
			
			
	