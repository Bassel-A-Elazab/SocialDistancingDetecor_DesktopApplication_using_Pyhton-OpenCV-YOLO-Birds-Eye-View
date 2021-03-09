package com.example.socialdistancenotification;

import androidx.annotation.RequiresApi;
import androidx.annotation.StringDef;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.viewpager.widget.ViewPager;

import android.content.Context;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.widget.ListView;
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
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {


    DetectedPeoplesList detectedPeoplesList = new DetectedPeoplesList();
    DetectedPeoplesListController detectedPeoplesListController = new DetectedPeoplesListController(detectedPeoplesList);
    ArrayList<DetectedPeoples> detectedPeoplesArrayList = new ArrayList<DetectedPeoples>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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

                            ListView mListView = (ListView) findViewById(R.id.listView);
                            DetectedPeoples detectedPeoples = null;
                            JSONObject jsonObj = null;

                            try {
                                jsonObj = new JSONObject(message);
                                String time = jsonObj.getString("time");
                                String count = jsonObj.getString("count");



                                detectedPeoples = new DetectedPeoples(null, LocalDate.now(), time, Integer.parseInt(count), null);

                                DetectedPeoplesList detectedPeoplesList = new DetectedPeoplesList();

                                boolean success = detectedPeoplesListController.addDetectedPeoples(detectedPeoples, MainActivity.this);
                                detectedPeoplesList.saveDetectedPeoples(MainActivity.this);
                                detectedPeoplesList.loadDetectedPeoples(MainActivity.this);
                                detectedPeoplesArrayList = detectedPeoplesListController.getDetectedPeoples();

                                DetectedPeoplesAdapter adapter = new DetectedPeoplesAdapter(MainActivity.this, R.layout.detectedpeopleslist_detectedpeoples, detectedPeoplesArrayList);

                                mListView.setAdapter(adapter);

                            }catch (JSONException e) {
                                e.printStackTrace();
                            }

                            Toast.makeText(getApplicationContext(), detectedPeoples.getTime(), Toast.LENGTH_SHORT).show();
                        }

                    });
                }

            }catch(IOException e){
                e.printStackTrace();
            }
        }
    }

}