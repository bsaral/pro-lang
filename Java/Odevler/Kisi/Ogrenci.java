
public class Ogrenci extends Kisi {
	private int sinif;
	private String bolum;
	private String sehir;
	
	public void setx(int a, String b, String c){
		sinif = a;
		bolum = b;
		sehir = c;
	}
	
	public void getx(){
		System.out.println("İsmi "+isim+" olan öğrenci "+sinif+" sınıfın "+bolum+" bölümünde ve memleketi "+sehir);
	}

}
