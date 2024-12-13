import java.util.*;
import java.util.stream.Collectors;

public class Day05 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "05";

    public Day05(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        Map<Integer, ArrayList<Integer>> rules = new HashMap<>();
        int i = 0;
        for (; i < this.lines.size(); i++){
            if(Objects.equals(this.lines.get(i), ""))
                break;

            String[] l = this.lines.get(i).split("\\|");
            Integer k = Integer.parseInt(l[0]);
            rules.computeIfAbsent(k, k1 -> new ArrayList<>());
            rules.get(k).add(Integer.parseInt(l[1]));
        }

        int sum = 0;
        i++;
        for (; i < this.lines.size(); i++){
            List<Integer> pages = Arrays.stream(lines.get(i).split(",")).mapToInt(Integer::parseInt).boxed().toList();
            List<Integer> alreadyUpdated = new ArrayList<>();
            boolean correct = true;
            for(Integer page : pages){
                ArrayList<Integer> rule = rules.get(page);
                alreadyUpdated.add(page);
                if(rule == null){
                    continue;
                }

                List<Integer> intersection = rule.stream().filter(alreadyUpdated::contains).toList();
                correct = correct && intersection.isEmpty();
            }
            if(correct){
                sum += pages.get(pages.size() / 2);
            }
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        Map<Integer, ArrayList<Integer>> rules = new HashMap<>();
        int i = 0;
        for (; i < this.lines.size(); i++){
            if(Objects.equals(this.lines.get(i), ""))
                break;

            String[] l = this.lines.get(i).split("\\|");
            Integer k = Integer.parseInt(l[0]);
            rules.computeIfAbsent(k, k1 -> new ArrayList<>());
            rules.get(k).add(Integer.parseInt(l[1]));
        }

        int sum = 0;
        i++;
        for (; i < this.lines.size(); i++){
            List<Integer> pages = Arrays.stream(lines.get(i).split(",")).mapToInt(Integer::parseInt).boxed().collect(Collectors.toList());
            List<Integer> alreadyUpdated = new ArrayList<>();
            boolean correct = true;
            for(int j = 0; j < pages.size(); j++){
                Integer page = pages.get(j);
                ArrayList<Integer> rule = rules.get(page);
                alreadyUpdated.add(page);
                if(rule == null){
                    continue;
                }

                List<Integer> intersection = rule.stream().filter(alreadyUpdated::contains).toList();
                correct = correct && intersection.isEmpty();
                if(!intersection.isEmpty()){
                    List<Integer> indices = intersection.stream().sorted(Comparator.comparing(pages::indexOf)).toList();
                    pages.remove(j);
                    pages.add(pages.indexOf(indices.getFirst()), page);
                }
            }

            if(!correct){
                sum += pages.get(pages.size() / 2);
            }
        }


        System.out.println("Solution Stage 2: " + sum);

    }
}
