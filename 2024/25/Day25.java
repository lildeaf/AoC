import java.util.ArrayList;
import java.util.List;

public class Day25 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "25";

    public Day25(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private static class Schematic{
        ArrayList<Integer> heights;

        public Schematic(List<String> scheme){
            heights = new ArrayList<>();
            for (int i = 0; i < scheme.getFirst().length(); i++)
                heights.add(0);

            for (String line : scheme){
                for (int i = 0; i < line.length(); i++)
                    heights.set(i, line.charAt(i) == '#' ? heights.get(i)+1 : heights.get(i));
            }
        }

        public boolean checkOverlap(Schematic schematic){
            for (int i = 0; i < heights.size(); i++){
                if(heights.get(i) + schematic.heights.get(i) > 5){
                    return true;
                }
            }

            return false;
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;
        ArrayList<Schematic> keys = new ArrayList<>();
        ArrayList<Schematic> locks = new ArrayList<>();

        for (int i = 0; i < this.lines.size(); i+=8){
            //System.out.println(i);
            String line = this.lines.get(i);
            if (line.charAt(0) == '.')
                keys.add(new Schematic(this.lines.subList(i+1, i+6).reversed()));
            else
                locks.add(new Schematic(this.lines.subList(i+1, i+6)));
        }

        for (Schematic lock: locks){
            for (Schematic key : keys){
                sum += key.checkOverlap(lock) ? 0 : 1;
            }
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int sum = 0;

        System.out.println("Solution Stage 2: " + sum);
    }
}
