import java.util.ArrayList;
import java.util.stream.IntStream;

public class Day02 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "02";

    public Day02(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private boolean checkWithout(String[] levels, int removed){
        String[] newList = IntStream
                .range(0, levels.length)
                .filter(j -> j != removed)
                .mapToObj(j -> levels[j])
                .toArray(String[]::new);

        return checkReport(newList, false);
    }

    private boolean checkReport(String[] levels, boolean dampener){
        int prev = Integer.parseInt(levels[0]), curr;
        boolean increasing = false;

        for(int i = 1; i < levels.length; i++){
            curr = Integer.parseInt(levels[i]);
            int diff = curr - prev;
            prev = curr;
            if(Math.abs(diff) > 3 || Math.abs(diff) < 1){
                if(!dampener)
                    return false;

                return checkWithout(levels, i) || checkWithout(levels, i - 1);
            }

            boolean currentIncreased = diff > 0;
            if(i == 1){
                increasing = currentIncreased;
                continue;
            }

            if(!(currentIncreased == increasing)){
                if(!dampener)
                    return false;


                return checkWithout(levels, i) || checkWithout(levels, i-1) || checkWithout(levels, i-2);
            }
        }

        return true;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");

        int safeReports = 0;
        for(String report : lines){
            String[] levels = report.split(" ");
            safeReports += checkReport(levels, false) ? 1 : 0;
        }

        System.out.println("Solution Stage 1: " + safeReports);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");

        int safeReports = 0;
        for(String report : lines){
            String[] levels = report.split(" ");
            safeReports += checkReport(levels, true) ? 1 : 0;
        }

        System.out.println("Solution Stage 1: " + safeReports);
    }
}
