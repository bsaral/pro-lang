package com.example.android;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;

public class Contract extends Activity {
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.contract);
		
		final CheckBox c1 = (CheckBox)findViewById(R.id.checkBox1);
		Button b1 = (Button)findViewById(R.id.button1);
		
		c1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				if(c1.isChecked()){
					c1.setEnabled(true);
				}
				else
					c1.setEnabled(false);
				
			}
		});
		
	}
}
