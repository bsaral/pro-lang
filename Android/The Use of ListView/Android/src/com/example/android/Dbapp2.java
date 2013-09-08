package com.example.android;

import android.R.string;
import android.app.Activity;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class Dbapp2 extends Activity {
	Button ekle;
	Button goster;
	Button sil;
	Button guncelle;
	EditText ad;
	EditText soyad;
	EditText yas;
	EditText sehir;
	TextView bilgiler;
	private Veritabani v2;
	
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.dbapp2);
		
		v2 = new Veritabani(this);
		ekle = (Button)findViewById(R.id.button1);
		goster = (Button)findViewById(R.id.button2);
		sil = (Button)findViewById(R.id.button3);
		guncelle = (Button)findViewById(R.id.button4);
		ad = (EditText)findViewById(R.id.editText1);
		soyad = (EditText)findViewById(R.id.editText2);
		yas = (EditText)findViewById(R.id.editText4);
		sehir = (EditText)findViewById(R.id.editText3);
		bilgiler = (TextView)findViewById(R.id.textView5);
		
		ekle.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				try{
					kayitekle(ad.getText().toString(), soyad.getText().toString(),yas.getText().toString(),sehir.getText().toString());
				}
				finally{
					v2.close();
				}
			}
		});
		
		goster.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				bilgileriGoster();
				
			}

		});
		
		sil.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				silme(ad.getText().toString());
				
			}
		});
		
		guncelle.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Guncelle(ad.getText().toString());
				
			}
		});
	}
	
	private void kayitekle(String ad, String soyad, String sehir, String yas){
		SQLiteDatabase db = v2.getWritableDatabase();
		ContentValues cv2 = new ContentValues();
		cv2.put("ad", ad);
		cv2.put("soyad",soyad);
		cv2.put("yas",yas);
		cv2.put("sehir",sehir);
		db.insertOrThrow("kisiler", null, cv2);
		
	}
	private String[] rows = {"ad","soyad","yas","sehir"};
	private String veriler = "";
	
	private void bilgileriGoster() {
		SQLiteDatabase db = v2.getReadableDatabase();
		Cursor okunanlar = db.query("kisiler", rows, null, null, null, null, null);
		while(okunanlar.moveToNext()){
			String name = okunanlar.getString(okunanlar.getColumnIndex("ad"));
			String sname = okunanlar.getString(okunanlar.getColumnIndex("soyad"));
			String country = okunanlar.getString(okunanlar.getColumnIndex("sehir"));
			int age = okunanlar.getInt(okunanlar.getColumnIndex("yas"));
			veriler = name+"\n"+sname+"\n"+country+"\n"+age+"\n";
			bilgiler.setText(veriler.toString());
		}
		
	}
	
	private void silme(String isim){
		SQLiteDatabase db = v2.getReadableDatabase();
		db.delete("kisiler", "ad"+"=?", new String [] { isim });
	}
	
	private void Guncelle(String isim){
		SQLiteDatabase db = v2.getWritableDatabase();
		ContentValues cv2 = new ContentValues();
		cv2.put("ad", isim);
		db.update("kisiler", cv2,"ad"+"=?", new String [] { isim });
		db.close();
	}
}
