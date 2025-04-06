import javax.swing.text.AttributeSet;
import java.lang.reflect.Array;
import java.math.BigInteger;
import java.util.*;

public class Day21 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "21";

    ArrayList<String> directional;
    HashMap<Character, Position> directions = new HashMap<>();

    HashMap<String, Long> cache = new HashMap<>();

    public Day21(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }

        this.directional = new ArrayList<>(Collections.nCopies(2, ".".repeat(3)));
        directions.put('^', new Position(1,0,this.directional));
        directions.put('v', new Position(1,1,this.directional));
        directions.put('<', new Position(0,1,this.directional));
        directions.put('>', new Position(2,1,this.directional));
    }

    private static class ButtonPress{
        Character key;
        int count;

        public ButtonPress(char c, int count){
            this.key = c;
            this.count = count;
        }

        @Override
        public String toString() {
            return "{" + key + ", "+ count + "}";
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            ButtonPress that = (ButtonPress) o;
            return key == that.key && count == that.count;
        }

        @Override
        public int hashCode() {
            return key*5 + count;
        }
    }

    private String buttonPress2(List<ButtonPress> presses, int robotCount){
        StringBuilder builder1 = new StringBuilder();
        Position currentKeyPad = new Position(2,0,this.directional);

        for (ButtonPress b : presses){
            int count = b.count;
            if (count == 0)
                continue;
            if (robotCount == 0){
                builder1.append(b.key.toString().repeat(count));
                continue;
            }

            Position keyPos = this.directions.get(b.key);

            int x = keyPos.getX() - currentKeyPad.getX();
            int y = keyPos.getY() - currentKeyPad.getY();
            char directionX = x < 0 ? '<' : '>';
            char directionY = y < 0 ? '^' : 'v';

            List<ButtonPress> presses2 = new ArrayList<>();
            boolean cheackDiff = false;

            if(x < 0){
                presses2.add(new ButtonPress(directionY, Math.abs(y)));
                presses2.add(new ButtonPress(directionX, Math.abs(x)));
                cheackDiff = !((currentKeyPad.getX() + x) == 0 && currentKeyPad.getY() == 0);
            } else {
                presses2.add(new ButtonPress(directionX, Math.abs(x)));
                presses2.add(new ButtonPress(directionY, Math.abs(y)));
                cheackDiff = !((currentKeyPad.getY() + y) == 0 && currentKeyPad.getX() == 0);
            }
            String sol1 = buttonPress2(presses2, robotCount-1);
            if (cheackDiff){
                String sol2 = buttonPress2(presses2.reversed(), robotCount-1);
                sol1 = sol1.length() < sol2.length() ? sol1 : sol2;
            }

            builder1.append(sol1);
            builder1.append("A".repeat(count));

            currentKeyPad = keyPos;
        }
        if(robotCount != 0){
            Position init = new Position(2,0,this.directional);
            int x = init.getX() - currentKeyPad.getX();
            int y = init.getY() - currentKeyPad.getY();
            char directionX = x < 0 ? '<' : '>';
            char directionY = y < 0 ? '^' : 'v';
            ArrayList<ButtonPress> presses2 = new ArrayList<>();
            presses2.add(new ButtonPress(directionX, Math.abs(x)));
            presses2.add(new ButtonPress(directionY, Math.abs(y)));
            builder1.append(buttonPress2(presses2, robotCount-1));
            //builder.append("A");
        }

        return builder1.toString();
    }

    private long buttonPress2Count(List<ButtonPress> presses, int robotCount){
        long result = 0;
        Position currentKeyPad = new Position(2,0,this.directional);
        String key = presses.toString() + robotCount;
        if (cache.containsKey(key))
            return cache.get(key);

        for (ButtonPress b : presses){
            int count = b.count;
            if (count == 0)
                continue;
            if (robotCount == 0){
                //builder1.append(b.key.toString().repeat(count));
                result += count;
                continue;
            }

            Position keyPos = this.directions.get(b.key);

            int x = keyPos.getX() - currentKeyPad.getX();
            int y = keyPos.getY() - currentKeyPad.getY();
            char directionX = x < 0 ? '<' : '>';
            char directionY = y < 0 ? '^' : 'v';

            List<ButtonPress> presses2 = new ArrayList<>();
            boolean cheackDiff = false;

            if(x < 0){
                presses2.add(new ButtonPress(directionY, Math.abs(y)));
                presses2.add(new ButtonPress(directionX, Math.abs(x)));
                cheackDiff = !((currentKeyPad.getX() + x) == 0 && currentKeyPad.getY() == 0);
            } else {
                presses2.add(new ButtonPress(directionX, Math.abs(x)));
                presses2.add(new ButtonPress(directionY, Math.abs(y)));
                cheackDiff = !((currentKeyPad.getY() + y) == 0 && currentKeyPad.getX() == 0);
            }
            long sol1 = buttonPress2Count(presses2, robotCount-1);
            if (cheackDiff){
                long sol2 = buttonPress2Count(presses2.reversed(), robotCount-1);
                sol1 = Math.min(sol1, sol2);
            }

            //builder1.append(sol1);
            result += sol1;
            //builder1.append("A".repeat(count));
            result += count;

            currentKeyPad = keyPos;
        }
        if(robotCount != 0){
            Position init = new Position(2,0,this.directional);
            int x = init.getX() - currentKeyPad.getX();
            int y = init.getY() - currentKeyPad.getY();
            char directionX = x < 0 ? '<' : '>';
            char directionY = y < 0 ? '^' : 'v';
            ArrayList<ButtonPress> presses2 = new ArrayList<>();
            presses2.add(new ButtonPress(directionX, Math.abs(x)));
            presses2.add(new ButtonPress(directionY, Math.abs(y)));
            long ret = buttonPress2Count(presses2, robotCount-1);
            //builder1.append(buttonPress2(presses2, robotCount-1));
            if (currentKeyPad.getX() != 0){
                long ret2 = buttonPress2Count(presses2.reversed(), robotCount-1);
                ret = Math.min(ret2, ret);
            }
            result += ret;
            //builder.append("A");
        }

        cache.put(key, result);

        return result;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;
        ArrayList<String> numeric = new ArrayList<>(Collections.nCopies(4, ".".repeat(3)));
        HashMap<Character, Position> keyPad = new HashMap<>();
        for (int i = 0; i < 9; i++){
            int num = i+1;
            int y = 2 - i / 3;
            int x = i%3;
            keyPad.put(String.valueOf(num).charAt(0), new Position(x,y,numeric));
        }

        keyPad.put('0', new Position(1, 3, numeric));
        keyPad.put('A', new Position(2, 3, numeric));

        System.out.println(keyPad);
        int robots = 2;

        for (String line : this.lines){
            Position current = new Position(2, 3, numeric);
            long buttonCount = 0;
            StringBuilder pressbuilder = new StringBuilder();
            for (int i = 0; i < line.length(); i++){
                Position n = keyPad.get(line.charAt(i));
                int x = n.getX() - current.getX();
                int y = n.getY() - current.getY();
                char directionX = x < 0 ? '<' : '>';
                char directionY = y < 0 ? '^' : 'v';
                List<ButtonPress> presses = new ArrayList<>();
                boolean cheackDiff = false;

                if(x < 0){
                    presses.add(new ButtonPress(directionY, Math.abs(y)));
                    presses.add(new ButtonPress(directionX, Math.abs(x)));
                    cheackDiff = !((current.getX() + x) == 0 && current.getY() == 3);

                }else {
                    presses.add(new ButtonPress(directionX, Math.abs(x)));
                    presses.add(new ButtonPress(directionY, Math.abs(y)));
                    cheackDiff = !((current.getY() + y) == 0 && current.getX() == 3);
                }

                //System.out.println(line.charAt(i) + " -> " +presses);
                String resss = buttonPress2(presses, robots) + "A";
                if (cheackDiff){
                    String sol2 = buttonPress2(presses.reversed(), robots) + "A";
                    resss = resss.length() < sol2.length() ? resss : sol2;
                }

                pressbuilder.append(resss);
                //System.out.println(line.charAt(i) + ": " + resss);
                current = n;
            }

            System.out.println(line + ": " + pressbuilder.toString());
            int complex = Integer.parseInt(line.substring(0, 3)) * pressbuilder.length();
            sum += complex;
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        cache.clear();
        System.out.println("Solving Stage 2...");
        BigInteger sum = BigInteger.ZERO;
        ArrayList<String> numeric = new ArrayList<>(Collections.nCopies(4, ".".repeat(3)));
        HashMap<Character, Position> keyPad = new HashMap<>();
        for (int i = 0; i < 9; i++){
            int num = i+1;
            int y = 2 - i / 3;
            int x = i%3;
            keyPad.put(String.valueOf(num).charAt(0), new Position(x,y,numeric));
        }

        keyPad.put('0', new Position(1, 3, numeric));
        keyPad.put('A', new Position(2, 3, numeric));

        System.out.println(keyPad);
        int robots = 25;

        for (String line : this.lines){
            Position current = new Position(2, 3, numeric);
            BigInteger buttonCount = BigInteger.ZERO;
            //StringBuilder pressbuilder = new StringBuilder();
            for (int i = 0; i < line.length(); i++){
                Position n = keyPad.get(line.charAt(i));
                int x = n.getX() - current.getX();
                int y = n.getY() - current.getY();
                char directionX = x < 0 ? '<' : '>';
                char directionY = y < 0 ? '^' : 'v';
                List<ButtonPress> presses = new ArrayList<>();
                boolean cheackDiff = false;

                if(x < 0){
                    presses.add(new ButtonPress(directionY, Math.abs(y)));
                    presses.add(new ButtonPress(directionX, Math.abs(x)));
                    cheackDiff = !((current.getX() + x) == 0 && current.getY() == 3);
                }else {
                    presses.add(new ButtonPress(directionX, Math.abs(x)));
                    presses.add(new ButtonPress(directionY, Math.abs(y)));
                    cheackDiff = !((current.getY() + y) == 0 && current.getX() == 3);
                }

                //System.out.println(line.charAt(i) + " -> " +presses);
                long resss = buttonPress2Count(presses, robots) + 1;
                if (cheackDiff){
                    long sol2 = buttonPress2Count(presses.reversed(), robots) + 1;
                    resss = Math.min(resss, sol2);
                }

                //pressbuilder.append(resss);
                //System.out.println(resss);
                buttonCount = buttonCount.add(new BigInteger(String.valueOf(resss)));
                //buttonCount += resss;
                //System.out.println(buttonCount);
                //System.out.println(line.charAt(i) + ": " + resss);
                current = n;
            }

            System.out.println(line + ": " + buttonCount);
            BigInteger complex = new BigInteger(line.substring(0, 3)).multiply(new BigInteger(String.valueOf(buttonCount)));
            sum = sum.add(complex);
        }


        System.out.println("Solution Stage 2: " + sum);
    }
}
