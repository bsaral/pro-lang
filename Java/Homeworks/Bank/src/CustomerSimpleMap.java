package coreservlets;

import java.util.*;

/** A small table of banking customers for testing. */

public class CustomerSimpleMap 
       implements CustomerLookupService {
  private Map<String,Customer> customers;

  public CustomerSimpleMap() {
    customers = new HashMap<String,Customer>();
    addCustomer(new Customer("id001", "Harry", 
                             "Hacker", -3456.78));
    addCustomer(new Customer("id002", "Codie",
                             "Coder", 1234.56));
    addCustomer(new Customer("id003", "Polly",
                             "Programmer", 987654.32));
  }

  /** Finds the customer with the given ID.
   *  Returns null if there is no match.
   */
  
  public Customer findCustomer(String id) {
    if (id!=null) {
      return(customers.get(id.toLowerCase()));
    } else {
      return(null);
    }
  }

  private void addCustomer(Customer customer) {
    customers.put(customer.getId(), customer);
  }
}
