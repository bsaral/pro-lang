
public class Test {
	public static void main(String[] args){
		Kisi kisi1 = new Kisi();
		kisi1.set("Betül", "SARAL", 20);
		kisi1.get();
		
		Memur memur1 = new Memur();
		memur1.setm(123, "abcd");
		memur1.set("Ercan", "ÖĞÜREN", 28);
		memur1.getm();
		memur1.uyur();
		
		Hoca hoca1 = new Hoca();
		hoca1.set("Hayri", "HAYRETETTİ", 35);
		hoca1.get();
		hoca1.sinav();
		
		Ogretim_Uyesi o1 = new Ogretim_Uyesi();
		o1.set("Hayriye", "OT", 28);
		o1.seto("mühendis");
		o1.geto();
		
		Ogrenci o2 = new Ogrenci();
		o2.set("Ayşe", "fatma", 22);
		o2.setx(3, "bilgisayar mühendisliği", "samsun");
		o2.getx();
	}
}
