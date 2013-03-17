
public class Hoca extends Kisi {
	private int sicil;
	private String bolum;
	
	public void seth(int x, String y){
		sicil = x;
		bolum = y;
	}
	
	public void geth(){
		System.out.println("İsim "+isim+" yas "+yas+ " sicilno "+sicil+" bölüm "+bolum);
	}
	
	public void sinav(){
		System.out.println("Hoca sınavı hazırlıyor.");
	}
}


