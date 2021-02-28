package com.example.socialdistancenotification;

import android.content.Context;

import java.util.ArrayList;

/**
 * DetectedPeoplesListController is responsible for all communication between views and DetectedPeoplesList object.
 */

public class DetectedPeoplesListController {

    private DetectedPeoplesList detectedPeoplesList;

    public DetectedPeoplesListController(DetectedPeoplesList detectedPeoplesList){
        this.detectedPeoplesList = detectedPeoplesList;
    }

    public void setDetectedPeoplesList(ArrayList<DetectedPeoples> detectedPeoples){
        this.detectedPeoplesList.setDetectedPeoples(detectedPeoples);
    }
    public ArrayList<DetectedPeoples> getDetectedPeoplesArrayList(){
        return detectedPeoplesList.getDetectedPeoples();
    }

    public boolean addDetectedPeoples(DetectedPeoples detectedPeoples, Context context){
        AddDetectedPeoplesCommand addDetectedPeoplesCommand = new AddDetectedPeoplesCommand(detectedPeoplesList, detectedPeoples, context);
        addDetectedPeoplesCommand.execute();
        return addDetectedPeoplesCommand.isExecuted();

    }

    public void loadDetectedPeoples(Context context){
        detectedPeoplesList.loadDetectedPeoples(context);
    }
}
