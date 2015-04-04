package com.mobisir.pool;

import android.app.Activity;
import android.os.Bundle;
import android.content.Intent;
import android.widget.Button;
import android.view.View;
import android.view.View.OnClickListener;

public class RegisterUser extends Activity
{
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.registration); 
        final Button join_user = (Button) findViewById(R.id.join_btn);
        join_user.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent i = new Intent(RegisterUser.this, PoolSearch.class);
                startActivity(i);
            }
        });
    }
}
