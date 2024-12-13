import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day07 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "07";

    public Day07(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    boolean checkStage1(Long result, Long current, List<Long> vals){
        if(current > result)
            return false;

        if(vals.isEmpty())
            return current.equals(result);

        return checkStage1(result, current * vals.getFirst(), vals.subList(1, vals.size())) ||
                checkStage1(result, current + vals.getFirst(), vals.subList(1, vals.size()));
    }

    boolean checkStage2(Long result, Long current, List<Long> vals){
        if(current > result)
            return false;

        if(vals.isEmpty())
            return current.equals(result);

        int l = String.valueOf(vals.getFirst()).length();
        long conc = (long) (current * Math.pow(10, l)) + vals.getFirst();

        return checkStage2(result, current * vals.getFirst(), vals.subList(1, vals.size())) ||
                checkStage2(result, current + vals.getFirst(), vals.subList(1, vals.size())) ||
                checkStage2(result, conc, vals.subList(1, vals.size()));
    }


    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");

        long sum = 0;
        for(String line : this.lines){
            String[] s = line.split(":");
            long result = Long.parseLong(s[0]);

            String[] nums = s[1].substring(1).split(" ");
            List<Long> t = Arrays.stream(nums).mapToLong(Long::parseLong).boxed().toList();

            if(checkStage1(result, t.getFirst(), t.subList(1, t.size())))
                sum += result;
        }
        System.out.println("Solution Stage 1 : " + sum);

    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");

        long sum = 0;
        for(String line : this.lines){
            String[] s = line.split(":");
            long result = Long.parseLong(s[0]);

            String[] nums = s[1].substring(1).split(" ");
            List<Long> t = Arrays.stream(nums).mapToLong(Long::parseLong).boxed().toList();

            if(checkStage2(result, t.getFirst(), t.subList(1, t.size())))
                sum += result;
        }

        System.out.println("Solution Stage 2: " + sum);

    }
}