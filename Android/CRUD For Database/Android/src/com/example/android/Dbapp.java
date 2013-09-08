package com.example.android;

import java.net.ContentHandler;

import android.app.Activity;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Dbapp extends Activity {
	Button b1;
	Button b2;
	EditText e1;
	EditText e2;
	TextView t1;
	TextView t2;
	private Veritabani v1;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.dbapp);
		
		v1 = new Veritabani(this);
		e1 = (EditText)findViewById(R.id.ad);
		e2 = (EditText)findViewById(R.id.soyad);
		t1 = (TextView)findViewById(R.id.ad1);
		t2 = (TextView)findViewById(R.id.ad2);
		b1= (Button)findViewById(R.id.kaydet);
		b2= (Button)findViewById(R.id.getir);
		
		b1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				try{
					ekleme(e1.getText().toString(),e2.getText().toString());
				}
				finally{
					v1.close();
				}
				
			}
		});
		
		b2.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				showinfos();
				
			}
		});
	}
	
	private void ekleme(String isim, String soyisim){
		SQLiteDatabase db = v1.getWritableDatabase();
		ContentValues cv1 = new ContentValues();
		cv1.put("ad", isim);
		cv1.put("soyad", soyisim);
		db.insertOrThrow("information", null, cv1);
	}

	private String[] rows={ "ad", "soyad"};
	private void showinfos(){
		SQLiteDatabase db = v1.getReadableDatabase();
		Cursor read = db.query("information", rows, null, null, null, null, null);
		while(read.moveToNext()){
			String name = read.getString(read.getColumnIndex("ad"));
			String sname = read.getString(read.getColumnIndex("soyad"));
			t1.setText(name);
			t2.setText(sname);
		}
		
	}
}
