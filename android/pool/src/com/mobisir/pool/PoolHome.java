package com.mobisir.pool;

import android.app.Activity;
import android.os.Bundle;
import android.content.Intent;

public class PoolHome extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        getActionBar().hide();
        new Thread() {
            public void run() {
                try {
                    	Intent i = new Intent(PoolHome.this,PoolSearch.class);
                        Thread.sleep(1500);
                        startActivity(i);
                        finish();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
        }.start();
    }
}
