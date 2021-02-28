package com.example.socialdistancenotification;

import android.graphics.Bitmap;

import java.util.Date;
import java.util.UUID;

/**
 * DetectedPeoplesController is responsible for all communication between views and Detected Peoples object
 */

public class DetectedPeoplesController {

    private DetectedPeoples detectedPeoples;

    public DetectedPeoplesController(DetectedPeoples detectedPeoples){
        this.detectedPeoples = detectedPeoples;
    }

    public String getDetectedID(){
        return detectedPeoples.getDetectedID();
    }
    public void setDetectedID(){
        detectedPeoples.setDetectedID();
    }

    public void setDetectedDate(Date detectedDate){
        detectedPeoples.setDetectedDate(detectedDate);
    }
    public Date getDetectedDate(){
        return detectedPeoples.getDetectedDate();
    }

    public void addImage(Bitmap new_image){
        detectedPeoples.addDetectedImage(new_image);
    }

    public Bitmap getImage(){
        return detectedPeoples.getDetectedImage();
    }

    public DetectedPeoples getDetectedPeoples() {
        return this.detectedPeoples;
    }

}
