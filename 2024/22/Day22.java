import java.util.ArrayList;

public class Day22 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "22";

    public Day22(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int sum = 0;

        System.out.println("Solution Stage 2: " + sum);
    }
}
