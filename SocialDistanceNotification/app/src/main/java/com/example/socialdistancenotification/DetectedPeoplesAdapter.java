package com.example.socialdistancenotification;

import android.content.Context;
import android.graphics.Bitmap;

import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * DetectedPeoplesAdapter is responsible for what information is displayed in ListView entries.
 */

public class DetectedPeoplesAdapter extends ArrayAdapter<DetectedPeoples> {

    private LayoutInflater inflater;
    private Fragment fragment;
    private Context context;

    public DetectedPeoplesAdapter(Context context, ArrayList<DetectedPeoples> objects, Fragment fragment) {
        super(context, 0, objects);
        this.context = context;
        this.inflater = LayoutInflater.from(context);
        this.fragment = fragment;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        // getItem(position) gets the "item" at "position" in the "items" ArrayList
        // (where "items" is a parameter in the ItemAdapter creator as seen above ^^)
        DetectedPeoples detectedPeoples = getItem(position);
        DetectedPeoplesController detectedPeoplesController = new DetectedPeoplesController(detectedPeoples);

        String date = "Date: " + detectedPeoplesController.getDate();
        String time = "Time: " + detectedPeoplesController.getTime();
        String countDetected = "Detected Count: " + detectedPeoplesController.getCountDetected();
        Bitmap thumbnail = detectedPeoplesController.getImage();

        // Check if an existing view is being reused, otherwise inflate the view.
        if (convertView == null) {
            convertView = inflater.from(context).inflate(R.layout.detectedpeopleslist_detectedpeoples, parent, false);
        }

        TextView date_tv = (TextView) convertView.findViewById(R.id.date_tv);
        TextView time_tv = (TextView) convertView.findViewById(R.id.time_tv);
        TextView countDetected_tv = (TextView) convertView.findViewById(R.id.count_tv);
        ImageView photo = (ImageView) convertView.findViewById(R.id.image_view);

        if (thumbnail != null) {
            photo.setImageBitmap(thumbnail);
        } else {
            photo.setImageResource(R.mipmap.ic_launcher_foreground);
        }

        date_tv.setText(date);
        time_tv.setText(time);
        countDetected_tv.setText(countDetected);

        return convertView;
    }
}

