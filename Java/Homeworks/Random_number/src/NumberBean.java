package coreservlets;

/** From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF 2.0, Ajax, GWT, and Java</a>.
 */

public class NumberBean {
  private final double num;

  public NumberBean(double number) {
    this.num = number;
  }
  
  public double getNumber() {
    return(num);
  }
}
