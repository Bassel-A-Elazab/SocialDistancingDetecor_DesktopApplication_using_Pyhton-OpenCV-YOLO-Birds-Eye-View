package com.example.socialdistancenotification;

import android.content.Context;

import java.util.ArrayList;

/**
 * DetectedPeoplesListController is responsible for all communication between views and Detected Peoples List object
 */

public class DetectedPeoplesListController {

    private DetectedPeoplesList detectedPeoplesList;

    public DetectedPeoplesListController(DetectedPeoplesList detectedPeoplesList){
        this.detectedPeoplesList = detectedPeoplesList;
    }

    public void setDetectedPeoples(ArrayList<DetectedPeoples> detectedPeoplesList) {
        this.detectedPeoplesList.setDetectedPeoples(detectedPeoplesList);
    }

    public ArrayList<DetectedPeoples> getDetectedPeoples() {
        return detectedPeoplesList.getDetectedPeoples();
    }

    public boolean addDetectedPeoples(DetectedPeoples item, Context context){
        AddDetectedPeoplesCommand add_item_command = new AddDetectedPeoplesCommand(detectedPeoplesList, item, context);
        add_item_command.execute();
        return add_item_command.isExecuted();
    }

    public void loadDetectedPeoples(Context context) {
        detectedPeoplesList.loadDetectedPeoples(context);
    }

}
