package hmwrk;

import java.util.*;

public class ShoppingCart {
	private ArrayList itemsOrdered;
	
	public ShoppingCart() {
		itemsOrdered = new ArrayList();
	}
	public List getItemsOrdered() {
		return(itemsOrdered);
	}
	public synchronized void addItem(String itemID) {
		ItemOrder order;
		for(int i=0; i<itemsOrdered.size(); i++) {
			order = (ItemOrder)itemsOrdered.get(i);
			if (order.getItemID().equals(itemID)) {
				order.incrementNumItems();
				return;
			}
		}
		ItemOrder newOrder = new ItemOrder(Catalog.getItem(itemID));
		itemsOrdered.add(newOrder);
	}
	public synchronized void setNumOrdered(String itemID,int numOrdered) {
		ItemOrder order;
		for(int i=0; i<itemsOrdered.size(); i++) {
			order = (ItemOrder)itemsOrdered.get(i);
			if (order.getItemID().equals(itemID)) {
				if (numOrdered <= 0) {
					itemsOrdered.remove(i);
				} 
				else {
					order.setNumItems(numOrdered);
				}
			return;
			}
		}
		ItemOrder newOrder = new ItemOrder(Catalog.getItem(itemID));
		itemsOrdered.add(newOrder);
	}
		
}
