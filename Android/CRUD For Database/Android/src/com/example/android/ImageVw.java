package com.example.android;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class ImageVw extends Activity {
	
	@Override
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.imagevw);
		
		Button res = (Button)findViewById(R.id.button1);
		final ImageView img = (ImageView)findViewById(R.id.imageView1);
		img.setVisibility(View.INVISIBLE);
		res.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				img.setImageResource(R.drawable.lale);
				img.setVisibility(View.VISIBLE);
				
			}
		});
	}
}
