package com.example.android;

import android.R.anim;
import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.RelativeLayout;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;

public class SeekBr extends Activity {
	
	SeekBar sb1,sb2,sb3;
	RelativeLayout r1;
	
	@Override
	
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.seekbr);
		
		sb1 = (SeekBar)findViewById(R.id.seekBar1);
		sb2 = (SeekBar)findViewById(R.id.seekBar2);
		sb3 = (SeekBar)findViewById(R.id.seekBar3);
		r1 = (RelativeLayout)findViewById(R.id.background);
	
		
		
		sb1.setOnSeekBarChangeListener(new OnSeekBarChangeListener() {
			
			@Override
			public void onStopTrackingTouch(SeekBar seekBar) {
				
				
			}
			
			@Override
			public void onStartTrackingTouch(SeekBar seekBar) {
				
				
			}
			
			@Override
			public void onProgressChanged(SeekBar seekBar, int progress,boolean fromUser) {
				sb1.setMax(255);
				int oran = android.graphics.Color.rgb(0, 0, progress);
				r1.setBackgroundColor(oran);
				
			}
		});
		
		sb2.setOnSeekBarChangeListener(new OnSeekBarChangeListener() {
			
			@Override
			public void onStopTrackingTouch(SeekBar seekBar) {
				
				
			}
			
			@Override
			public void onStartTrackingTouch(SeekBar seekBar) {
				
				
			}
			
			@Override
			public void onProgressChanged(SeekBar seekBar, int progress,
					boolean fromUser) {
				sb2.setMax(255);
				int oran2 = android.graphics.Color.rgb(0, progress, 0);
				r1.setBackgroundColor(oran2);
				
				
			}
		});
		
		sb3.setOnSeekBarChangeListener(new OnSeekBarChangeListener() {
			
			@Override
			public void onStopTrackingTouch(SeekBar seekBar) {
				
			}
			
			@Override
			public void onStartTrackingTouch(SeekBar seekBar) {
				
			}
			
			@Override
			public void onProgressChanged(SeekBar seekBar, int progress,
					boolean fromUser) {
				
				sb3.setMax(255);
				int oran3 = android.graphics.Color.rgb(progress, 0, 0);
				r1.setBackgroundColor(oran3);
			}
		});
		
	}
	
	

}
