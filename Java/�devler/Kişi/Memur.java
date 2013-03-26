
public class Memur extends Kisi{
	private int sicilno;
	private String bolum;
	
	public void setm(int x, String y){
		sicilno = x;
		bolum = y;
	}
	
	public void getm(){
		System.out.println("İsim "+isim+" yas "+yas+ " sicilno "+sicilno+" bölüm "+bolum);
	}
	
	public void evrak(){
		System.out.println("evrağı getirdim götürdüm");
	}
}
