package com.example.socialdistancenotification;
import android.content.Context;

/**
 * Command to add Detected Peoples come from Pyhton-Opencv.
 */

public class AddDetectedPeoplesCommand extends Command{

    private DetectedPeoplesList detectedPeoplesList;
    private DetectedPeoples detectedPeoples;
    private Context context;

    public AddDetectedPeoplesCommand(DetectedPeoplesList detectedPeoplesList, DetectedPeoples detectedPeoples, Context context) {
        this.detectedPeoplesList = detectedPeoplesList;
        this.detectedPeoples = detectedPeoples;
        this.context = context;
    }

    public void execute(){
        detectedPeoplesList.addDetectedPeoples(detectedPeoples);
        setIsExecuted(detectedPeoplesList.saveDetectedPeoples(context));
    }
}
