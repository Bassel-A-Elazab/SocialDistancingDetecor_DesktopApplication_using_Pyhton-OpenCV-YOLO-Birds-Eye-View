package com.example.socialdistancenotification;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.viewpager.widget.ViewPager;

import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.widget.Toast;

import com.google.android.material.tabs.TabLayout;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.time.LocalDate;

public class MainActivity extends AppCompatActivity {

    DetectedPeoplesList detectedPeoplesList = new DetectedPeoplesList();
    DetectedPeoplesListController detectedPeoplesListController = new DetectedPeoplesListController(detectedPeoplesList);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        // Create the adapter that will return a fragment for each of the three
        // primary sections of the activity.
        SectionsPagerAdapter mSectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());

        // Set up the ViewPager with the sections adapter.
        ViewPager mViewPager = (ViewPager) findViewById(R.id.container);
        mViewPager.setAdapter(mSectionsPagerAdapter);
        mViewPager.setOffscreenPageLimit(0);

        TabLayout tabLayout = (TabLayout) findViewById(R.id.tabs);
        tabLayout.setupWithViewPager(mViewPager);

        Thread myThread = new Thread(new MyServerThread());
        myThread.start();
    }

    class MyServerThread implements Runnable {

        Socket socket;
        ServerSocket serverSocket;
        InputStreamReader inputStreamReader;
        BufferedReader bufferedReader;
        Handler handler = new Handler();
        String message;

        @Override
        public void run() {

            try{
                serverSocket = new ServerSocket(7802);
                while(true){

                    socket = serverSocket.accept();
                    inputStreamReader = new InputStreamReader(socket.getInputStream());
                    bufferedReader = new BufferedReader(inputStreamReader);
                    message = bufferedReader.readLine();
                    handler.post(new Runnable() {

                        @RequiresApi(api = Build.VERSION_CODES.O)
                        @Override
                        public void run() {

                            JSONObject jsonObj = null;

                            try {
                                jsonObj = new JSONObject(message);

                                LocalDate date = LocalDate.now();
                                String time = jsonObj.getString("time");
                                String count = jsonObj.getString("count");

                                DetectedPeoples detectedPeoples = new DetectedPeoples(null, date, time, Integer.parseInt(count), null);
                                boolean success = detectedPeoplesListController.addDetectedPeoples(detectedPeoples, MainActivity.this);
				if(!success){
					Toast.makeText(getApplicationContext(), "Falied To send", Toast.LENGTH_SHORT).show();
				}

                            }catch (JSONException e) {
                                e.printStackTrace();
                            }

                            Toast.makeText(getApplicationContext(), "Success", Toast.LENGTH_SHORT).show();
                        }

                    });
                }

            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }

}
