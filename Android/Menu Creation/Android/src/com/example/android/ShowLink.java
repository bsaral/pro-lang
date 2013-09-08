package com.example.android;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;

public class ShowLink extends Activity {
	WebView w1;
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.showlink);
		w1 = (WebView)findViewById(R.id.webView1);
		w1.loadUrl(getIntent().getExtras().getString(Link_Variable.link));
	}

}
