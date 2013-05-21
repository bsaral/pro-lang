package coreservlets;

import java.math.BigInteger;

/** A bean that stores a prime BigInteger. Immutable.
 *  <p>
 *  From <a href="http://courses.coreservlets.com/Course-Materials/">the
 *  coreservlets.com tutorials on servlets, JSP, Struts, JSF, Ajax, GWT, 
 *  Spring, Hibernate/JPA, and Java programming</a>.
 */

public class PrimeBean {
  private BigInteger prime;

  public PrimeBean(String lengthString) {
    int length = 150;
    try {
      length = Integer.parseInt(lengthString);
    } catch(NumberFormatException nfe) {}
    this.prime = Primes.nextPrime(Primes.random(length));
  }

  public BigInteger getPrime() {
    return(prime);
  }
}
