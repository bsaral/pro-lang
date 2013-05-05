package hmwrk;

import javax.swing.JApplet;

public class applet extends JApplet {
	public void init(){
		WindowUtilities.setNativeLookAndFeel();
		setContentPane(new textpanel());
	}
	

}
