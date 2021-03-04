package com.example.socialdistancenotification;

import android.content.Context;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Type;
import java.util.ArrayList;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

/**
 * detectedPeoplesList class
 */

public class DetectedPeoplesList {

    private static ArrayList<DetectedPeoples> detectedPeoplesList;
    private String FILENAME = "detectedPeoples.sav";

    public DetectedPeoplesList() {
        detectedPeoplesList = new ArrayList<DetectedPeoples>();
    }

    public void setDetectedPeoples(ArrayList<DetectedPeoples> detectedPeoples) {
        detectedPeoplesList = detectedPeoples;
    }

    public ArrayList<DetectedPeoples> getDetectedPeoples() {
        return detectedPeoplesList;
    }

    public void addDetectedPeoples(DetectedPeoples detectedPeoples) {
        detectedPeoplesList.add(detectedPeoples);
    }

    public void loadDetectedPeoples(Context context) {

        try {
            FileInputStream fis = context.openFileInput(FILENAME);
            InputStreamReader isr = new InputStreamReader(fis);
            Gson gson = new Gson();
            Type listType = new TypeToken<ArrayList<DetectedPeoples>>() {
            }.getType();
            detectedPeoplesList = gson.fromJson(isr, listType); // temporary
            fis.close();
        } catch (FileNotFoundException e) {
            detectedPeoplesList = new ArrayList<DetectedPeoples>();
        } catch (IOException e) {
            detectedPeoplesList = new ArrayList<DetectedPeoples>();
        }
    }

    public boolean saveDetectedPeoples(Context context) {
        try {
            FileOutputStream fos = context.openFileOutput(FILENAME, 0);
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            Gson gson = new Gson();
            gson.toJson(detectedPeoplesList, osw);
            osw.flush();
            fos.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return false;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }

}



