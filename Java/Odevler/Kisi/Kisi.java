
public class Kisi {
	public String isim;
	private String soyisim;
	public int yas;
	
	public void set(String x, String y, int z){
		this.isim = x;
		this.soyisim = y;
		this.yas = z;
	}
	
	public void get(){
		String cumle = "İsim "+isim+" soyisim "+soyisim+" yas "+yas;
		System.out.println(cumle);
	}
	
	public void uyur(){
		System.out.println(this.isim+" uyuyor");
	}
	
	public void gezer(){
		System.out.println(this.isim+" geziyor");
	}

}

