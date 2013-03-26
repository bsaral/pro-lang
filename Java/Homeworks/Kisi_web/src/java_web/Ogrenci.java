package java_web;

public class Ogrenci extends Kisi {
	private int sinif;
	private String bolum;
	private String sehir;

	public void setx(int a, String b, String c){
		sinif = a;
		bolum = b;
		sehir = c;
	}

	public String getx(){
		return "Ad "+isim+" olan ogrenci "+sinif+" sinifin "+bolum+" bolumunde ve memleketi "+sehir;
	}

}
