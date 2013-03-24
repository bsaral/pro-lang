package java_web;

public class Memur extends Kisi{
	private int sicilno;
	private String bolum;

	public void setm(int x, String y){
		sicilno = x;
		bolum = y;
	}

	public String getm(){
		String cumle =("Ad "+isim+" yas "+yas+ " sicilno "+sicilno+" bolum "+bolum);
		return cumle;
	}

	public void evrak(){
		System.out.println("evraðý getirdim götürdüm");
	}
}
