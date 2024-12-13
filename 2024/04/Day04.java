import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Day04 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "04";

    public Day04(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    public int checkHorizontal(String letters, int xIndex){
        char[] chars = {'M', 'A', 'S'};
        boolean[] xmas = {true, true};
        for (int i = 0; i < 3; i++){
            xmas[0] = xmas[0] && (((xIndex - 1) - i) >= 0) &&
                    (letters.charAt((xIndex - 1)-i) == chars[i]);
            xmas[1] = xmas[1] && ((xIndex + 1) + i) < letters.length() &&
                    (letters.charAt((xIndex + 1)+i) == chars[i]);
        }

        return (xmas[0] ? 1 : 0) + (xmas[1] ? 1 : 0);
    }

    public int checkVertical(int x, int y){
        char[] chars = {'M', 'A', 'S'};
        boolean[] xmas = {true, true};
        for (int i = 1; i < 4; i++){
            xmas[0] = xmas[0] && (y - i) >= 0 &&
                    (this.lines.get(y - i).charAt(x) == chars[i-1]);
            xmas[1] = xmas[1] && (y + i) < this.lines.size() &&
                    (this.lines.get(y + i).charAt(x) == chars[i-1]);
        }

        return (xmas[0] ? 1 : 0) + (xmas[1] ? 1 : 0);
    }

    public int checkDiagonal(int x, int y, int letterLength){
        char[] chars = {'M', 'A', 'S'};
        boolean[] xmas = {true, true, true, true};
        for (int i = 1; i < 4; i++){
            xmas[0] = xmas[0] &&
                    (y - i) >= 0 &&
                    (x - i) >= 0 &&
                    this.lines.get(y - i).charAt(x - i) == chars[i-1];

            xmas[1] = xmas[1] &&
                    (y - i) >= 0 &&
                    (x + i) < letterLength &&
                    this.lines.get(y - i).charAt(x + i) == chars[i-1];

            xmas[2] = xmas[2] &&
                    (y + i) < this.lines.size() &&
                    (x - i) >= 0 &&
                    this.lines.get(y + i).charAt(x - i) == chars[i-1];

            xmas[3] = xmas[3] &&
                    (y + i) < this.lines.size() &&
                    (x + i) < letterLength &&
                    this.lines.get(y + i).charAt(x + i) == chars[i-1];
        }
        //System.out.println(xIndex + " - " + Arrays.toString(xmas));
        return (xmas[0] ? 1 : 0) +
                (xmas[1] ? 1 : 0) +
                (xmas[2] ? 1 : 0) +
                (xmas[3] ? 1 : 0);
    }

    public int checkMas(int x, int y, int letterLength){
        if(y - 1 < 0 || x - 1 < 0 || x + 1 == letterLength || y+1 == this.lines.size())
            return 0;

        Set<Character> charSet = new HashSet<>(Arrays.asList('M', 'S'));

        char leftTop = this.lines.get(y-1).charAt(x-1);
        char rightTop = this.lines.get(y-1).charAt(x+1);

        char leftBot = this.lines.get(y+1).charAt(x-1);
        char rightBot = this.lines.get(y+1).charAt(x+1);

        return (charSet.contains(leftTop) && charSet.contains(rightBot) && leftTop != rightBot &&
                charSet.contains(rightTop) && charSet.contains(leftBot) && rightTop != leftBot) ? 1 : 0;
    }


    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int letterLength = this.lines.getFirst().length();
        int sum = 0;
        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for (int x = 0; x < letterLength; x++){
                if(line.charAt(x) != 'X')
                    continue;

                sum += checkHorizontal(line, x) +
                        checkVertical(x, y) +
                        checkDiagonal(x, y, letterLength);
            }
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int letterLength = this.lines.getFirst().length();
        int sum = 0;
        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for (int x = 0; x < letterLength; x++){
                if(line.charAt(x) != 'A')
                    continue;

                sum += checkMas(x, y, letterLength);
            }
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
