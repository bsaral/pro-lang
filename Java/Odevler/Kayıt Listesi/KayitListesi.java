import java.awt.JobAttributes;
import java.util.ArrayList;

import javax.swing.JOptionPane;


public class KayitListesi {
	ArrayList liste = new ArrayList();
	
	private void basla (){
		this.ekran();
	}
	
	private void ekran(){
		String yazi = "Seçiminizi yapınız:\n***********************\n";
		yazi += "\n[1] İsim ekle";
		yazi += "\n[2] isim sil";
		yazi += "\n[3] listeyi göster";
		
		String secimstr  = this.giris(yazi);
		int secim = Integer.parseInt(secimstr);
		
		switch(secim){
		case 1: this.ekle();break;
		case 2: this.sil();break;
		case 3: this.goster();break;
		default: JOptionPane.showMessageDialog(null, "yanlış seçim yaptınız");
		this.ekran();break;
		}
		
	}
	
	
	public String giris(String str){
		return JOptionPane.showInputDialog(null,str);
	}
	
	
	private void ekle(){
		String ekle = this.giris("ismi giriniz");
		if (ekle != null )
			liste.add(ekle.toUpperCase());
		else
			JOptionPane.showMessageDialog(null, "lütfen bir isim giriniz");
		
		this.ekran();
	}
	
	
	private void sil(){
		String sil = this.giris("silinecek ismi giriniz");
		if (sil != null){
			if (liste.indexOf(sil) == -1 )
				JOptionPane.showMessageDialog(null, "listede böyle bir kayıt bulunmamaktadır");
			else {
				liste.remove(sil);
				JOptionPane.showMessageDialog(null, "isim silindi");
			}	
		}
		else
			JOptionPane.showMessageDialog(null, "lütfen isim giriniz");
		
		this.ekran();
	}
	
	private void goster(){
		String goster = "liste\n**************\n";
		for (int i = 0; i < liste.size(); i++){
			goster += liste.get(i);
		}
		JOptionPane.showMessageDialog(null, goster);
		this.ekran();
	}
	
	
	public static void main(String[] args){
		KayitListesi a = new KayitListesi();
		a.basla();
	}
}
