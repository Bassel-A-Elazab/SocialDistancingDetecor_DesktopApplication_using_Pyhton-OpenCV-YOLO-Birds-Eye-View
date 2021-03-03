package com.example.socialdistancenotification;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.util.Base64;

import java.io.ByteArrayOutputStream;
import java.util.UUID;

/**
 * DetectedPeoples class
 */

public class DetectedPeoples extends Observable {

    private String Id;
    private String date;
    protected transient Bitmap image;
    protected String image_base64;


    public DetectedPeoples(String Id, String date, Bitmap image) {

        this.date = date;
        addImage(image);

        if (Id == null){
            setId();
        } else {
            updateId(Id);
        }
    }

    public String getId(){
        return this.Id;
    }

    public void setId() {
        this.Id = UUID.randomUUID().toString();
        notifyObservers();
    }

    public void updateId(String id){
        this.Id = id;
        notifyObservers();
    }

    public void setDate(String date) {
        this.date = date;
        notifyObservers();
    }

    public String getDate() {
        return date;
    }

    public void addImage(Bitmap new_image){
        if (new_image != null) {
            image = new_image;
            ByteArrayOutputStream byteArrayBitmapStream = new ByteArrayOutputStream();
            new_image.compress(Bitmap.CompressFormat.PNG, 100, byteArrayBitmapStream);

            byte[] b = byteArrayBitmapStream.toByteArray();
            image_base64 = Base64.encodeToString(b, Base64.DEFAULT);
        }
        notifyObservers();
    }

    public Bitmap getImage(){
        if (image == null && image_base64 != null) {
            byte[] decodeString = Base64.decode(image_base64, Base64.DEFAULT);
            image = BitmapFactory.decodeByteArray(decodeString, 0, decodeString.length);
            notifyObservers();
        }
        return image;
    }
}
