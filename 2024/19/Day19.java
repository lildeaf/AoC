import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Day19 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "19";

    HashMap<String, Long> poss = new HashMap<>();

    public Day19(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private boolean isDesignPossible(String design, HashMap<Character, Set<String>> towels){
        if (design.isEmpty())
            return true;

        char c = design.charAt(0);
        Set<String> towelSet = towels.getOrDefault(c, new HashSet<>());
        for (String towel: towelSet){
            if(!design.startsWith(towel))
                continue;

            if(isDesignPossible(design.substring(towel.length()) ,towels))
                return true;
        }

        return false;
    }

    private long possibleDesigns(String design, HashMap<Character, Set<String>> towels){
        if (design.isEmpty())
            return 1;

        if(poss.containsKey(design))
            return poss.get(design);

        char c = design.charAt(0);
        Set<String> towelSet = towels.getOrDefault(c, new HashSet<>());
        long possible = 0;
        for (String towel: towelSet){
            if(!design.startsWith(towel))
                continue;

            possible += possibleDesigns(design.substring(towel.length()) ,towels);
        }

        long p = poss.getOrDefault(design, (long)0);
        poss.put(design, p+possible);

        return possible;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;

        HashMap<Character, Set<String>> towels = new HashMap<>();
        String[] s = this.lines.getFirst().split(", ");
        for (String towel : s){
            char c = towel.charAt(0);
            Set<String> current = towels.getOrDefault(c, new HashSet<>());
            current.add(towel);
            towels.put(c, current);
        }

        for (int i= 2; i < this.lines.size(); i++){
            boolean check = isDesignPossible(this.lines.get(i), towels);
            sum += check ? 1 : 0;
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        long sum = 0;

        HashMap<Character, Set<String>> towels = new HashMap<>();
        String[] s = this.lines.getFirst().split(", ");
        for (String towel : s){
            char c = towel.charAt(0);
            Set<String> current = towels.getOrDefault(c, new HashSet<>());
            current.add(towel);
            towels.put(c, current);
        }

        for (int i= 2; i < this.lines.size(); i++){
            sum += possibleDesigns(this.lines.get(i), towels);
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
