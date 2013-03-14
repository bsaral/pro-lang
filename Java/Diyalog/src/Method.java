
import javax.swing.JOptionPane;


public class Method {
	public static void main(String arg[]){
		String mesaj;
		int uzunluk;
		boolean compare,esitlik;
		
		mesaj = JOptionPane.showInputDialog(null, "Ruh halini gir :");
		
		esitlik = "mutlu".equals(mesaj);
		
		if (esitlik) {
			JOptionPane.showConfirmDialog(null, "guzeeeeel :)");
			
		} else {
			JOptionPane.showConfirmDialog(null, ":-o");
		}
		
		System.exit(0);
		
	}

}
