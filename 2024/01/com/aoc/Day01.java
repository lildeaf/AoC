package com.aoc;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Day01 implements Day{
    private final InputHelper inputHelper;
    ArrayList<String> lines;

    private static final String DAY = "01";

    private ArrayList<Integer> list1;
    private ArrayList<Integer> list2;

    public Day01(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        initInput();
    }

    private void initInput(){
        this.list1 = new ArrayList<Integer>();
        this.list2 = new ArrayList<Integer>();

        for (String line : lines){
            String[] l = line.split(" {3}");
            list1.add(Integer.valueOf(l[0]));
            list2.add(Integer.valueOf(l[1]));
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        Collections.sort(this.list1);
        Collections.sort(this.list2);

        int difference = 0;
        for (int i = 0; i < list1.size(); i++){
            difference += Math.abs(list1.get(i) - list2.get(i));
        }

        System.out.println("Solution Stage 1: " + difference);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        HashMap<Integer, Integer> countMap = new HashMap<Integer, Integer>();
        for(Integer id : list2){
            countMap.compute(id , (k, count) -> (count == null) ? 1 : (count + 1));
        }

        int similarity = 0;
        for(Integer id : list1){
            similarity += (id * countMap.getOrDefault(id, 0));
        }

        System.out.println("Solution Stage 2: " + similarity);
    }
}
