package hmwrk;

public class book extends CatalogPage {
	public void init() {
		String[] ids = { "olaylar", "ismail", "piston" };
		setItems(ids);
		setTitle("Kitaplar Listesi");
	}
}
