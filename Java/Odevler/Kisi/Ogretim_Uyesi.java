
public class Ogretim_Uyesi extends Hoca {
	private String unvan;
	
	public void seto (String c){
		unvan = c;
	}
	
	public void geto(){
		System.out.println(isim+" isimli hocanın "+unvan+" unvanlı öğrtim görevlisi vardır");
	}
}
