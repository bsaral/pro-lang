package com.example.android;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class Aktarim extends Activity{
	TextView t1 ;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.aktarim);
		
		t1 = (TextView)findViewById(R.id.textView2);
		Bundle al = getIntent().getExtras();
		String alinmis = al.getString("veri");
		t1.setText(alinmis);
		
	}

}
