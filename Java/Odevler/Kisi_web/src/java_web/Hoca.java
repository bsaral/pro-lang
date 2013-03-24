package java_web;

public class Hoca extends Kisi {
	private int sicil;
	private String bolum;

	public void seth(int x, String y){
		sicil = x;
		bolum = y;
	}

	public void geth(){
		System.out.println("Ad "+isim+" yas "+yas+ " sicilno "+sicil+" bölüm "+bolum);
	}

	public String sinav(){
		return "Hoca sinavi hazirliyor.";
	}
}

