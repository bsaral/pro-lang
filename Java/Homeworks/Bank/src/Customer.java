package coreservlets;

/** Bean to represent a bank customer. Immutable.
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, 
 *  Spring, Hibernate/JPA, and Java programming</a>.
 */

public class Customer {
  private final String id, firstName, lastName;
  private final double balance;

  public Customer(String id,
                  String firstName,
                  String lastName,
                  double balance) {
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;
    this.balance = balance;
  }
  
  public String getId() {
    return id;
  }

  public String getFirstName() {
    return(firstName);
  }

  public String getLastName() {
    return(lastName);
  }

  public double getBalance() {
    return(balance);
  }

  public String getBalanceNoSign() {
    String balanceString = 
      String.format("%,.2f", Math.abs(balance));
    return(balanceString);
  }
}
  
