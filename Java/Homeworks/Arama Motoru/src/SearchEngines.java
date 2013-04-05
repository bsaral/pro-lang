package web;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/SearchEngines")
public class SearchEngines extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		PrintWriter out = response.getWriter();
		 String searchString = request.getParameter("searchString");
		    
		    searchString = URLEncoder.encode(searchString, "utf-8");
		    String searchEngineName = request.getParameter("searchEngine");
		    if ((searchEngineName == null) || (searchEngineName.length() == 0)) {
		      out.println("Missing search engine name");
		      
		    }
		    String searchURL = Secenekler.makeURL(searchEngineName, searchString);
		    if (searchURL != null) {
		      response.sendRedirect(searchURL);
		    } 
		    else {
		      out.println("Unrecognized search engine");
		    } 
		}
	}
