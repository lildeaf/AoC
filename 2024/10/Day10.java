import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Day10 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "10";

    public Day10(boolean testing) {
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if (this.lines == null) {
            System.exit(-1);
        }
    }

    private Set<Position> checkTrails(Position current){
        Set<Position> result = new HashSet<>();
        char c = this.lines.get(current.getY()).charAt(current.getX());
        if(c == 0x39)
        {
            result.add(current);
            return result;
        }

        //check neighbors
        Set<Position> neighbors = current.getNeighborsInBounds(this.lines); // neighbors in bound
        for(Position neighbor : neighbors){
            char neighbor_c = this.lines.get(neighbor.getY()).charAt(neighbor.getX());
            if(neighbor_c == c+1){
                result.addAll(checkTrails(neighbor));
            }
        }

        return result;
    }

    private int checkDistinctTrails(Position current){
        int result = 0;
        char c = this.lines.get(current.getY()).charAt(current.getX());
        if(c == 0x39)
        {
            return 1;
        }

        //check neighbors
        Set<Position> neighbors = current.getNeighborsInBounds(this.lines); // neighbors in bound
        for(Position neighbor : neighbors){
            char neighbor_c = this.lines.get(neighbor.getY()).charAt(neighbor.getX());
            if(neighbor_c == c+1){
                result += checkDistinctTrails(neighbor);
            }
        }

        return result;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");

        int sum = 0;

        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x = 0; x < line.length(); x++){
                if(line.charAt(x) != '0')
                    continue;

                Set<Position> p = checkTrails(new Position(x, y));
                sum += p.size();
            }
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");

        int sum = 0;

        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x = 0; x < line.length(); x++){
                if(line.charAt(x) != '0')
                    continue;

                sum += checkDistinctTrails(new Position(x, y));
            }
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
