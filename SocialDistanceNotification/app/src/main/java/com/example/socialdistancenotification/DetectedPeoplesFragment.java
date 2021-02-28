package com.example.socialdistancenotification;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import androidx.fragment.app.Fragment;

import java.util.ArrayList;

/**
 * Superclass of DetectedPeoplesFragment
 */

public abstract class DetectedPeoplesFragment extends Fragment {

    private DetectedPeoplesList detectedPeoplesList = new DetectedPeoplesList();
    DetectedPeoplesListController detectedPeoplesController = new DetectedPeoplesListController(detectedPeoplesList);

    View rootView;
    private ListView listView;
    private ArrayAdapter<DetectedPeoples> adapter;
    private ArrayList<DetectedPeoples> selectedDetected;
    private LayoutInflater inflater;
    private ViewGroup container;
    private Context context;
    private Fragment fragment;
    private boolean update = false;


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        context = getContext();

        // Don't update view yet. Wait until after items have been filtered.
        detectedPeoplesList.loadDetectedPeoples(context);
        update = true;

        this.inflater = inflater;
        this.container = container;

        return rootView;
    }

    public void loadDetectedPeoples(Fragment fragment){
        this.fragment = fragment;
        detectedPeoplesList.loadDetectedPeoples(context);
    }
}
