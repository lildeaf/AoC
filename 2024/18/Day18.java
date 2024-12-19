import java.util.*;

public class Day18 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    boolean testing;

    ArrayList<String> map;

    private static final String DAY = "18";

    public Day18(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }

        int size = testing ? 7 : 71;
        map = new ArrayList<>(Collections.nCopies(size, ".".repeat(size)));
        this.testing = testing;
    }

    private class PositionState {
        Position p;
        int currentSteps;


        public PositionState(Position p, int steps){
            this.p = p;
            this.currentSteps = steps;
        }

        @Override
        public String toString() {
            return p.toString() + ", " + currentSteps;
        }
    }

    private void printMap(Set<Position> bytes){
        for (int y = 0; y < this.map.size(); y++){
            String line = this.map.get(y);
            for (int x = 0; x < line.length(); x++){
                System.out.print(bytes.contains(new Position(x,y, this.map)) ? '#' : '.');
            }
            System.out.println();
        }
    }

    public boolean checkPath(Set<Position> bytes){
        Position end = new Position(this.map.getFirst().length()-1, this.map.size()-1, this.map);
        Position start = new Position(0, 0, this.map);
        Set<Position> visited = new HashSet<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentSteps));
        queue.add(new PositionState(start, 0));

        while (!queue.isEmpty()){
            PositionState current = queue.poll();
            if(current.p.equals(end)){
                return true;
            }

            Position p = current.p;
            if(visited.contains(p)){
                continue;
            }
            visited.add(p);

            for (Position newPos : p.getNeighborsInBounds()){
                if(bytes.contains(newPos))
                    continue;

                queue.add(new PositionState(newPos, current.currentSteps+1));
            }
        }

        return false;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int result = 0;
        Set<Position> bytes = new HashSet<>();

        for (int i = 0; i < (testing ? 12 : 1024); i++){
            String[] b = this.lines.get(i).split(",");
            bytes.add(new Position(Integer.parseInt(b[0]), Integer.parseInt(b[1]), this.map));
        }
        
        Position end = new Position(this.map.getFirst().length()-1, this.map.size()-1, this.map);
        Position start = new Position(0, 0, this.map);

        Set<Position> visited = new HashSet<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentSteps));
        queue.add(new PositionState(start, 0));

        while (true){
            PositionState current = queue.poll();
            if(current.p.equals(end)){
                result = current.currentSteps;
                break;
            }

            Position p = current.p;
            if(visited.contains(p)){
                continue;
            }
            visited.add(p);

            for (Position newPos : p.getNeighborsInBounds()){
                if(bytes.contains(newPos))
                    continue;

                queue.add(new PositionState(newPos, current.currentSteps+1));
            }
        }


        System.out.println("Solution Stage 1: " + result);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        ArrayList<Position> bytes = new ArrayList<>();

        for (int i = 0; i < this.lines.size(); i++){
            String[] b = this.lines.get(i).split(",");
            bytes.add(new Position(Integer.parseInt(b[0]), Integer.parseInt(b[1]), this.map));
        }

        int l = 0, r = this.lines.size();
        int first = 0;
        while (true){
            int check = l + (r-l) / 2;

            boolean foundPath = checkPath(new HashSet<>(bytes.subList(0, check)));
            if(foundPath) l = check;
            else r = check;

            if(r-l == 1){
                first = r;
                if(!foundPath)
                    first = l;
                break;
            }
        }

        System.out.println("Solution Stage 2: " + bytes.get(first-1));
    }
}
