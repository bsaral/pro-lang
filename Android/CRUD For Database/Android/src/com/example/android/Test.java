package com.example.android;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

public class Test extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.test);
		
		final RadioButton r1 = (RadioButton)findViewById(R.id.radioButton1);
		final RadioButton r2 = (RadioButton)findViewById(R.id.radioButton2);
		final RadioButton r3 = (RadioButton)findViewById(R.id.radioButton3);
		
		final CheckBox c1 = (CheckBox)findViewById(R.id.checkBox1);
		final CheckBox c2 = (CheckBox)findViewById(R.id.checkBox2);
		final CheckBox c3 = (CheckBox)findViewById(R.id.checkBox3);
		
		final Button goster = (Button)findViewById(R.id.button1);
		
		goster.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				String metin = "";
				if(r1.isChecked()){
					metin = metin + "Sarýyý Seviyorsun";
				}
				else if (r2.isChecked()){
					metin += "Turkuazý Seviyorsun";
				}
				else{
					metin += "Moru Seviyorsun";
				}
				
				if(c1.isChecked()){
					metin = metin + "Java Biliyorsun";
				}
				if (c2.isChecked()){
					metin += "Python Biliyorsun";
				}
				if (c3.isChecked()){
					metin += "Ruby Seviyorsun";
				}
				
				Toast.makeText(getApplicationContext(), metin, Toast.LENGTH_LONG).show();
			}
		});

	}

}
