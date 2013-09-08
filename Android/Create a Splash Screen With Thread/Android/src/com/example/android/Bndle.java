package com.example.android;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Bndle extends Activity {
	
	EditText e1;
	Button b1;
	Bundle bnd;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.bundle);
		
		
		b1 = (Button)findViewById(R.id.button1);
		bnd = new Bundle();
		e1 = (EditText)findViewById(R.id.editText1);
		final Intent i = new Intent(getApplicationContext(),Aktarim.class);
		
		b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				String aktar = e1.getText().toString();
				bnd.putString("veri", aktar);
				i.putExtras(bnd);
				startActivity(i);
				
			}
		});
	}
}
