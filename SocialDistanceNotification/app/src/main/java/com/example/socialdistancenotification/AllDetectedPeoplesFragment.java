package com.example.socialdistancenotification;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;

public class AllDetectedPeoplesFragment extends DetectedPeoplesFragment{

    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){

        super.onCreateView(inflater, container, savedInstanceState);
        super.setVariables(R.layout.all_detectedpeoples_fragment, R.id.my_detectedPeoples);
        super.loadDetectedPeoples(AllDetectedPeoplesFragment.this);

        return rootView;
    }

    @Override
    public ArrayList<DetectedPeoples> filterDetectedPeoples() {
        return detectedPeoplesListController.getDetectedPeoplesArrayList();
    }
}
