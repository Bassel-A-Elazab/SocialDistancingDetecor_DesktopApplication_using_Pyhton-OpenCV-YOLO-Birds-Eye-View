package com.example.socialdistancenotification;

import android.content.Context;
import android.graphics.Bitmap;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.fragment.app.Fragment;

import java.util.ArrayList;
import java.util.Date;


public class DetectedPeoplesAdapter extends ArrayAdapter<DetectedPeoples> {

    private LayoutInflater inflater;
    private Fragment fragment;
    private Context context;

    public DetectedPeoplesAdapter(Context context, ArrayList<DetectedPeoples> detectedPeoples, Fragment fragment) {

        super(context, 0, detectedPeoples);
        this.context = context;
        this.inflater = LayoutInflater.from(context);
        this.fragment = fragment;
    }

    public View getView(int position, View convertView, ViewGroup parent){

        // getDetectedPeoples (position) gets the "detected people" at "position" in the "DetectedPeoples" ArrayList
        // (where "DetectedPeoples" is a parameter in the DetectedPeoplesAdapter creator as seen above ^^)
        DetectedPeoples detectedPeoples = getItem(position);
        DetectedPeoplesController detectedPeoplesController = new DetectedPeoplesController(detectedPeoples);

        Date date = detectedPeoplesController.getDetectedDate();
        Bitmap thumbnail = detectedPeoplesController.getImage();

        // Check if an existing view is being reused, otherwise inflate the view.
        if(convertView == null){
            convertView = inflater.from(context).inflate(R.layout.detectedpeopleslist_detectedpeoples, parent);
        }

        TextView date_tv = (TextView) convertView.findViewById(R.id.date);
        ImageView photo = (ImageView) convertView.findViewById(R.id.image_view);

        if(thumbnail != null){
            photo.setImageBitmap(thumbnail);
        }else{
            photo.setImageResource(android.R.drawable.ic_menu_gallery);
        }

        date_tv.setText(date_tv.toString());

        return convertView;
    }
}
