package java_web;

public class Kisi {
	
	public String isim;
	private String soyisim;
	public int yas;

	public void set(String x, String y, int z){
		this.isim = x;
		this.soyisim = y;
		this.yas = z;
	}

	public String get(){
		String cumle = "Ad "+isim+" soyad "+soyisim+" yas "+yas;
		return cumle;
		
	}

	public String uyur(){
		return this.isim+" uyuyor";
	}

	public void gezer(){
		System.out.println(this.isim+" geziyor");
	}

}

