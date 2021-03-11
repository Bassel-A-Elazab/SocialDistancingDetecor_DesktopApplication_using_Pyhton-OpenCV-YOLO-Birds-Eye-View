package com.example.socialdistancenotification;

import android.content.Context;
import android.os.Bundle;
import androidx.fragment.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;

/**
 * Superclass of DetectedPeoplesFragment
 */

public abstract class DetectedPeoplesFragment extends Fragment {

    private DetectedPeoplesList detectedPeoplesList = new DetectedPeoplesList();
    DetectedPeoplesListController detectedPeoplesListController = new DetectedPeoplesListController(detectedPeoplesList);

    View rootView;
    private ListView list_view;
    private ArrayAdapter<DetectedPeoples> adapter;
    private ArrayList<DetectedPeoples> selected_items;
    private LayoutInflater inflater;
    private ViewGroup container;
    private Context context;
    private Fragment fragment;
    private boolean update = false;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        context = getContext();

        // Don't update view yet. Wait until after items have been filtered.
        detectedPeoplesListController.loadDetectedPeoples(context);
        update = true;

        this.inflater = inflater;
        this.container = container;

        return rootView;
    }

    public void setVariables(int resource, int id ) {
        rootView = inflater.inflate(resource, container, false);
        list_view = (ListView) rootView.findViewById(id);
        selected_items = filterItems();

    }

    public void loadItems(Fragment fragment){
        this.fragment = fragment;
        detectedPeoplesListController.loadDetectedPeoples(context);
        update();
    }

    public abstract ArrayList<DetectedPeoples> filterItems();

    /**
     * Update the view
     */
    public void update(){
        if (update) {
            adapter = new DetectedPeoplesAdapter(context, selected_items, fragment);
            list_view.setAdapter(adapter);
            adapter.notifyDataSetChanged();
        }
    }
}
