import javax.swing.JOptionPane;
import javax.xml.bind.annotation.XmlElementDecl.GLOBAL;


public class guess_number {
	
	public void player(int co_number){
		String isim = JOptionPane.showInputDialog("İsminizi giriniz : ");
		JOptionPane.showMessageDialog(null,"Merhaba "+isim+" Oyuna hoşgeldin :) \n 1-100 arasında bilgisayarın belirlediği sayıyı tahmin ediceksin.3 hakkın var\n");
		int cevap = JOptionPane.showConfirmDialog(null, "Hazırsan başlayalım mı ?");
		if (cevap == 0){
			int count = 1;
			while (count <= 3 ){
				int number = Integer.parseInt(JOptionPane.showInputDialog(count+".Sayıyı giriniz :"));
				if (number == co_number ){
					JOptionPane.showMessageDialog(null, "TEBRİKLER UYDURDUN TUTTU");
					break;
				}
				count += 1;
			}
			JOptionPane.showMessageDialog(null, "Sayımız : "+co_number+" olucaktı.KAZANAMADIN AHAHAH");
		}
		else
			JOptionPane.showMessageDialog(null, "Madem oynamak istemiyorsun güle güle");
		}

	
	public static void main(String[] args) {
		int c_number = (int) (Math.random() * 100);
		guess_number start = new guess_number();
		start.player(c_number);
		
		
	}

}
