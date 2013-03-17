import java.util.Arrays;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;


public class Dizi {
	public static void main(String[] args){
		int boyut = Integer.parseInt(JOptionPane.showInputDialog("Liste kaç elemandan oluşsun ?"));
		String liste[] = liste(boyut);
		Goster(liste);
		Max_Min(liste);
		Ortalama(liste);
	}

	public static String[] liste(int uzunluk){
		String sayilar[] = new String[uzunluk];
		
		for (int i = 0; i < sayilar.length; i++)
			sayilar[i] = JOptionPane.showInputDialog(i+".sayıyı giriniz");
		
		Arrays.sort(sayilar);
		return sayilar;
		
	}
	
	public static void Max_Min(String dizi[]){
		int max,min,uzunluk;
	    Arrays.sort(dizi);
	    uzunluk = dizi.length;
		max = Integer.parseInt(dizi[uzunluk-1]);
		min = Integer.parseInt(dizi[0]);
		String sonuc = "En büyük eleman "+max+" en küçük eleman "+min;
		JOptionPane.showMessageDialog(null, sonuc);
		
	}
	
	public static void Ortalama(String dizi[]){
		int toplam = 0;
		String ortalama;
		for (int i = 0; i < dizi.length; i++){
			toplam += Integer.parseInt(dizi[i]);
		}
		
		ortalama = "Dizi ortalaması"+(toplam / dizi.length);
		JOptionPane.showMessageDialog(null, ortalama);
	}
	
	public static void Goster(String dizi[]){
		JTextArea ekran = new JTextArea(15,15);
		String cikis = "Küçükten Büyüğe \n";

		for(int i = 0; i < dizi.length; i++){
			cikis += dizi[i] + "\n";
		}
		
		ekran.setText(cikis);
		JOptionPane.showMessageDialog(null, ekran);
	}
}
