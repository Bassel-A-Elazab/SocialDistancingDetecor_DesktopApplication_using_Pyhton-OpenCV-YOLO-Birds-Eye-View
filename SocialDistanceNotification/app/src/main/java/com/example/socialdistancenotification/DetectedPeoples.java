package com.example.socialdistancenotification;

import android.graphics.Bitmap;

import java.io.ByteArrayOutputStream;

import android.graphics.BitmapFactory;
import android.util.Base64;
import java.util.Date;
import java.util.UUID;

public class DetectedPeoples {
    private String detectedID;
    private Date detectedDate;
    protected transient Bitmap detectedImage;
    protected String image_base64;

    public DetectedPeoples(String detectedID, Date detectedDate, Bitmap detectedImage){

        this.detectedDate = detectedDate;
        this.detectedImage = detectedImage;
        addDetectedImage(detectedImage);
        if(detectedID == null){
            setDetectedID();
        }else{
            updateID(detectedID);
        }
    }

    public String getDetectedID(){
        return this.detectedID;
    }
    public void setDetectedID(){
        this.detectedID = UUID.randomUUID().toString();
    }
    public void updateID(String detectedID){
        this.detectedID = detectedID;
    }

    public void setDetectedDate(Date detectedDate){
        this.detectedDate = detectedDate;
    }
    public Date getDetectedDate(){
        return this.detectedDate;
    }

    public void addDetectedImage(Bitmap newImage){
        if(newImage != null){
            detectedImage = newImage;
            ByteArrayOutputStream byteArrayBitmapStream = new ByteArrayOutputStream();
            newImage.compress(Bitmap.CompressFormat.PNG, 100, byteArrayBitmapStream);

            byte[] b = byteArrayBitmapStream.toByteArray();
            image_base64 = Base64.encodeToString(b, Base64.DEFAULT);
        }
    }

    public Bitmap getDetectedImage(){
        if (detectedImage == null && image_base64 != null) {
            byte[] decodeString = Base64.decode(image_base64, Base64.DEFAULT);
            detectedImage = BitmapFactory.decodeByteArray(decodeString, 0, decodeString.length);
        }
        return detectedImage;
    }

}
