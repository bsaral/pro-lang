package coreservlets;

import java.math.BigInteger;

public class Primes {
 
  private static final BigInteger ZERO = BigInteger.ZERO;
  private static final BigInteger ONE = BigInteger.ONE;
  private static final BigInteger TWO = new BigInteger("2");
  
 
  private static final int ERR_VAL = 100;
  
  public static BigInteger nextPrime(BigInteger start) {
    if (isEven(start))
      start = start.add(ONE);
    else
      start = start.add(TWO);
    if (start.isProbablePrime(ERR_VAL))
      return(start);
    else
      return(nextPrime(start));
  }

  private static boolean isEven(BigInteger n) {
    return(n.mod(TWO).equals(ZERO));
  }

  private static StringBuffer[] digits =
    { new StringBuffer("0"), new StringBuffer("1"),
      new StringBuffer("2"), new StringBuffer("3"),
      new StringBuffer("4"), new StringBuffer("5"),
      new StringBuffer("6"), new StringBuffer("7"),
      new StringBuffer("8"), new StringBuffer("9") };

  private static StringBuffer randomDigit(boolean isZeroOK) {
    int index;
    if (isZeroOK) {
      index = (int)Math.floor(Math.random() * 10);
    } else {
      index = 1 + (int)Math.floor(Math.random() * 9);
    }
    return(digits[index]);
  }

 
  
  public static BigInteger random(int numDigits) {
    StringBuffer s = new StringBuffer("");
    for(int i=0; i<numDigits; i++) {
      if (i == 0) {
        // First digit must be non-zero.
        s.append(randomDigit(false)); 
      } else {
        s.append(randomDigit(true));
      }
    }
    return(new BigInteger(s.toString()));
  }

  
  
  public static void main(String[] args) {
    int numDigits;
    try {
      numDigits = Integer.parseInt(args[0]);
    } catch (Exception e) { // No args or illegal arg.
      numDigits = 150;
    }
    BigInteger start = random(numDigits);
    for(int i=0; i<50; i++) {
      start = nextPrime(start);
      System.out.println("Prime " + i + " = " + start);
    }
  }
}
