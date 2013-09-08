package com.example.android;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class Veritabani extends SQLiteOpenHelper{
	
	public static final String VERITABANI_ADI ="android.db";
	public static final int SURUM=1;
	public Veritabani(Context c){
		super(c,VERITABANI_ADI,null,SURUM);
	}
	@Override
	public void onCreate(SQLiteDatabase db) {
		db.execSQL("CREATE TABLE information(ad TEXT,soyad TEXT);");
		
	}
	@Override
	public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
		db.execSQL("DROP TABLE IF EXIST information");
		onCreate(db);
		
	}
}
