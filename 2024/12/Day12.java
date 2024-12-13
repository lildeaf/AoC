import java.util.*;

public class Day12 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    final Set<Position> visited = new HashSet<>();

    private static final String DAY = "12";

    public Day12(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private int checkRegion(Position current, char plant, Set<Position> region){
        if(region.contains(current))
            return 0;

        if(current.outOfBounds(this.lines) || this.lines.get(current.getY()).charAt(current.getX()) != plant)
            return 1;

        region.add(current);
        visited.add(current);
        Set<Position> neighbors = current.getAllNeighbors();
        int sum = 0;
        for (Position neighbor : neighbors){
            sum += checkRegion(neighbor, plant, region);
        }

        return sum;
    }

    private int countEdges(Set<Position> area){
        int corners = 0;

        for(Position p : area){
            ArrayList<Boolean> surrounding = new ArrayList<>();
            for (int y = -1; y < 2; y++){
                for (int x = -1; x < 2; x++){
                    surrounding.add(area.contains(new Position(p.getX() + x, p.getY() + y)));
                }
            }
            /*
                Surrounding indices of A:

                0 1 2
                3 A 5
                6 7 8

                  !1 !3
                  !1 !5

                !0 1 3
                !2 1 5

                  !7 !3
                  !7 !5

                6 7 3
                8 7 5
             */


            for(int i = 1; i<8; i += 6){
                for(int j = 3; j<6; j += 2) {
                    if(!surrounding.get(i) && !surrounding.get(j))
                        corners++;

                    int cornerIndex = j==3 ? i - 1: i + 1;
                    if(!surrounding.get(cornerIndex) && surrounding.get(i) && surrounding.get(j))
                        corners++;
                }
            }
        }

        return corners;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;
        visited.clear();
        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x = 0; x < line.length(); x++){
                Position p = new Position(x,y);
                if (visited.contains(p))
                    continue;

                Set<Position> region = new HashSet<>();
                int perimeter = checkRegion(p, line.charAt(x), region);
                sum += region.size() * perimeter;
            }
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        visited.clear();
        int sum = 0;
        for(int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x = 0; x < line.length(); x++){
                Position p = new Position(x,y);
                if (visited.contains(p))
                    continue;

                Set<Position> region = new HashSet<>();
                checkRegion(p, line.charAt(x), region);
                int edges = countEdges(region);
                sum += region.size() * edges;
            }
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
