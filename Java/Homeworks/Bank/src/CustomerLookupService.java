package coreservlets;

/** Main interface for classes that let you retrieve bank
 *  customers by ID. This interface provides no way to
 *  modify the set of customers, so you don't have to
 *  worry about race conditions with shared data.
 */

public interface CustomerLookupService {
  public Customer findCustomer(String id);
}
