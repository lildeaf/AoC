import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day03 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "03";

    public Day03(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        String memory = String.join("", this.lines);
        String regex = "mul\\((\\d{1,3}),(\\d{1,3})\\)";

        Matcher matcher = Pattern.compile(regex).matcher(memory);

        int sum = 0;
        while(matcher.find()){
            sum += Integer.parseInt(matcher.group(1)) * Integer.parseInt(matcher.group(2));
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        String memory = String.join("", this.lines);
        String regex = "mul\\((\\d{1,3}),(\\d{1,3})\\)|(?<instr>do|don't)\\(\\)";

        Matcher matcher = Pattern.compile(regex).matcher(memory);

        int sum = 0;
        boolean enabled = true;
        while(matcher.find()){
            String instr = matcher.group("instr");
            if(instr != null)
                enabled = instr.equals("do");
            else
                sum += !enabled ? 0 : Integer.parseInt(matcher.group(1)) * Integer.parseInt(matcher.group(2));

        }

        System.out.println("Solution Stage 2: " + sum);
    }

}
