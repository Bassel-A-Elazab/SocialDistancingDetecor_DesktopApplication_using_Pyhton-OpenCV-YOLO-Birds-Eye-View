package com.example.socialdistancenotification;

import android.graphics.Bitmap;

import java.time.LocalDate;

/**
 * DetectedPeoplesController is responsible for all communication between views and Detected Peoples object
 */

public class DetectedPeoplesController {

    private DetectedPeoples detectedPeoples;

    public DetectedPeoplesController(DetectedPeoples detectedPeoples){
        this.detectedPeoples = detectedPeoples;
    }

    public String getId(){
        return detectedPeoples.getId();
    }

    public void setId() {
        detectedPeoples.setId();
    }

    public void setDate(LocalDate date) {
        detectedPeoples.setDate(date);
    }

    public LocalDate getDate(){
        return detectedPeoples.getDate();
    }

    public void setCountDetected(int countDetected){
        detectedPeoples.setCountDetected(countDetected);
    }
    public int getCountDetected(){
        return detectedPeoples.getCountDetected();
    }

    public void setTime(String time){
        detectedPeoples.setTime(time);
    }
    public String getTime(){
        return detectedPeoples.getTime();
    }

    public void addImage(Bitmap new_image){
        detectedPeoples.addImage(new_image);
    }

    public Bitmap getImage(){
        return detectedPeoples.getImage();
    }

    public DetectedPeoples getDetectedPeoples() { return this.detectedPeoples; }

}
