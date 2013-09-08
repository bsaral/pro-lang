package com.example.android;


import android.media.MediaPlayer;
import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;


public class MainActivity extends Activity {
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.splash);
		
		Thread t1 = new Thread()
		{
			public void run(){
				try {
					sleep(3000);
					Intent i = new Intent("android.intent.action.SPLASH");
					startActivity(i);
				} catch (InterruptedException e1) {
					// TODO: handle exception
				}
				finally {
					finish();
				}
			}
		};
		t1.start();
	

		
		Button goster = (Button)findViewById(R.id.button1);
		Button test = (Button)findViewById(R.id.button2);
		Button con = (Button)findViewById(R.id.button3);
		Button renk = (Button)findViewById(R.id.button4);
		Button img = (Button)findViewById(R.id.button5);
		Button web = (Button)findViewById(R.id.button6);
		Button db = (Button)findViewById(R.id.button7);
		Button db2 = (Button)findViewById(R.id.button8);
		Button bundle = (Button)findViewById(R.id.button9);
		Button liste = (Button)findViewById(R.id.button10);
		
		liste.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.LISTE"));
				
			}
		});
		
		bundle.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.BNDLE"));
				
			}
		});
		
		db2.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.DBAPP2"));
				
			}
		});
		
		db.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.DBAPP"));
				
			}
		});
		
		web.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.WEB"));
				
			}
		});
		
		img.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.IMAGEVW"));
				
			}
		});
		
		renk.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.SEEKBR"));
				
			}
		});
		
		con.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.CONTRACT"));
				
			}
		});
		
		test.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				startActivity(new Intent("android.intent.action.TEST"));
				
			}
		});
		
		goster.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				startActivity(new Intent("android.intent.action.RESIM"));
				
			}
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		super.onCreateOptionsMenu(menu);
		MenuInflater m = getMenuInflater();
		m.inflate(R.menu.sayfa, menu);
		return super.onCreateOptionsMenu(menu);
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch (item.getItemId()) {
		case R.id.item1:
			System.exit(0);
			return true;

		case R.id.item2:
			startActivity(new Intent("android.intent.action.TEST"));
			return true;
		}
		return false;
	}
	
	
	 

	
}
