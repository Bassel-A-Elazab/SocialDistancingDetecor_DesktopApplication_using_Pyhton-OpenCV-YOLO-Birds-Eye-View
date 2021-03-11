package com.example.socialdistancenotification;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Build;
import android.util.Base64;

import androidx.annotation.RequiresApi;

import java.io.ByteArrayOutputStream;
import java.time.LocalDate;
import java.util.UUID;

/**
 * DetectedPeoples class
 */

@RequiresApi(api = Build.VERSION_CODES.O)
public class DetectedPeoples{

    private String Id;
    private LocalDate date;
    private String time;
    private int countDetected;

    protected transient Bitmap image;
    protected String image_base64;


    public DetectedPeoples(String Id, LocalDate date, String time, int countDetected, Bitmap image) {

        this.date = LocalDate.now();
        this.time = time;
        this.countDetected = countDetected;
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
    }

    public void updateId(String id){
        this.Id = id;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public LocalDate getDate() {
        return LocalDate.now();
    }

    public void setTime(String time){
        this.time = time;
    }
    public String getTime(){
        return this.time;
    }

    public void setCountDetected(int countDetected){
        this.countDetected = countDetected;
    }
    public int getCountDetected(){
        return this.countDetected;
    }

    public void addImage(Bitmap new_image){
        if (new_image != null) {
            image = new_image;
            ByteArrayOutputStream byteArrayBitmapStream = new ByteArrayOutputStream();
            new_image.compress(Bitmap.CompressFormat.PNG, 100, byteArrayBitmapStream);

            byte[] b = byteArrayBitmapStream.toByteArray();
            image_base64 = Base64.encodeToString(b, Base64.DEFAULT);
        }
    }

    public Bitmap getImage(){
        if (image == null && image_base64 != null) {
            byte[] decodeString = Base64.decode(image_base64, Base64.DEFAULT);
            image = BitmapFactory.decodeByteArray(decodeString, 0, decodeString.length);
        }
        return image;
    }
}
