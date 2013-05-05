package hmwrk;

import java.awt.BorderLayout;
import java.awt.GraphicsEnvironment;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JApplet;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class textpanel extends JApplet implements ActionListener {
	private JComboBox fontBox;
	private DrawingPanel drawingPanel;
	public textpanel() {
	GraphicsEnvironment env = GraphicsEnvironment.getLocalGraphicsEnvironment(); 
	String[] fontNames = env.getAvailableFontFamilyNames();
	fontBox = new JComboBox(fontNames);
	setLayout(new BorderLayout());
	JPanel fontPanel = new JPanel();
	fontPanel.add(new JLabel("Font:"));
	fontPanel.add(fontBox);
	JButton drawButton = new JButton("Draw");
	drawButton.addActionListener(this);
	fontPanel.add(drawButton);
	add(fontPanel, BorderLayout.SOUTH);
	drawingPanel = new DrawingPanel();
	fontBox.setSelectedItem("Serif");
	drawingPanel.setFontName("Serif");
	add(drawingPanel, BorderLayout.CENTER);
	}
	public void actionPerformed1(ActionEvent e) {
	drawingPanel.setFontName((String)fontBox.getSelectedItem());
	drawingPanel.repaint();
	}
	@Override
	public void actionPerformed(ActionEvent arg0) {
		// TODO Auto-generated method stub
		
	}

	

}
