package com.example.android;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Web extends Activity {
	
	Button b;
	EditText e;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.web);
		
		e = (EditText)findViewById(R.id.editText1);
		b = (Button)findViewById(R.id.butonlink);
		
		b.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Intent i1 = new Intent(Web.this,ShowLink.class);
				i1.putExtra(Link_Variable.link, e.getText().toString());
				startActivity(i1);
				
			}
		});
	}
}
