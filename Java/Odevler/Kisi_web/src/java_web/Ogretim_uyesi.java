package java_web;

public class Ogretim_uyesi extends Hoca {
	private String unvan;

	public void seto (String c){
		unvan = c;
	}

	public void geto(){
		System.out.println(isim+" isimli hocan�n "+unvan+" unvanl� ��rtim g�revlisi vard�r");
	}
}
