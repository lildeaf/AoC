import java.util.*;
import java.util.function.Function;

public class Day20 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "20";

    //HashMap<Position ,HashMap<Integer, HashSet<PositionState>>> cache = new HashMap();

    public Day20(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
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


    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        Position start = new Position(this.lines);
        Position end = new Position(this.lines);
        for(int y =0 ; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x =0 ; x < line.length(); x++){
                if (line.charAt(x) == 'S')
                    start = new Position(x,y,this.lines);

                if (line.charAt(x) == 'E')
                    end = new Position(x,y,this.lines);
            }
        }

        HashMap<Position, PositionState> visited = new HashMap<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentSteps));
        queue.add(new PositionState(start, 0));
        HashMap<Integer, Integer> cheats = new HashMap<>();

        while (true){
            PositionState current = queue.poll();
            Position p = current.p;

            //check cheat to current;
            for (Position neighbor : p.getNeighborsInBounds()){
                if(this.lines.get(neighbor.getY()).charAt(neighbor.getX()) != '#')
                    continue;

                for(Position cheat : neighbor.getNeighborsInBounds()){
                    if(!visited.containsKey(cheat))
                        continue;


                    PositionState s = visited.get(cheat);
                    int diff = current.currentSteps - s.currentSteps;
                    diff -= 2;
                    if (diff <= 0)
                        continue;
                    int count = cheats.getOrDefault(diff, 0);
                    cheats.put(diff, count+1);
                }
            }

            if(p.equals(end)){
                break;
            }


            visited.put(p, current);

            for (Position newPos : p.getNeighborsInBounds()){
                if(this.lines.get(newPos.getY()).charAt(newPos.getX()) == '#')
                    continue;

                if(visited.containsKey(newPos)){
                    continue;
                }

                queue.add(new PositionState(newPos, current.currentSteps+1));
            }
        }

        System.out.println(cheats);
        int result = 0;

        for (int k : cheats.keySet()){
            result += k < 100 ? 0 : cheats.get(k);
        }

        System.out.println("Solution Stage 1: " + result);
    }


    private HashSet<Position> cache = new HashSet<>();
    private HashSet<Position> checkCheat(Position current, int time, HashMap<Position, PositionState> visited){
        if (time <= 0 || cache.contains(current))
            return new HashSet<>();

        HashSet<Position> cheats = new HashSet<>();

        for(Position cheat : current.getNeighborsInBounds()){
            if(cheat.outOfBounds())
                continue;
            cheats.addAll(checkCheat(cheat, time-1, visited));

            if(!visited.containsKey(cheat))
                continue;

            cheats.add(cheat);
        }

        cache.add(current);

        return cheats;
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        Position start = new Position(this.lines);
        Position end = new Position(this.lines);
        for(int y =0 ; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for(int x =0 ; x < line.length(); x++){
                if (line.charAt(x) == 'S')
                    start = new Position(x,y,this.lines);

                if (line.charAt(x) == 'E')
                    end = new Position(x,y,this.lines);
            }
        }

        HashMap<Position, PositionState> visited = new HashMap<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentSteps));
        queue.add(new PositionState(start, 0));
        HashMap<Integer, Integer> cheats = new HashMap<>();

        while (true){
            PositionState current = queue.poll();
            Position p = current.p;

            //System.out.println(p);
            HashSet<Position> cheatPositions = new HashSet<>();
            //check cheat to current;
            for (Position vis : visited.keySet()){
                if (Math.abs(vis.getX() - p.getX()) + Math.abs(vis.getY() - p.getY()) > 20)
                    continue;

                cheatPositions.add(vis);
            }
            for (Position cheatPos : cheatPositions){
                PositionState state = visited.get(cheatPos);
                int diff = current.currentSteps - state.currentSteps;
                diff -= Math.abs(p.getX() - state.p.getX()) + Math.abs(p.getY() - state.p.getY());
                if (diff <= 99)
                    continue;

                int count = cheats.getOrDefault(diff, 0);
                cheats.put(diff, count+1);
            }


            if(p.equals(end)){
                break;
            }

            visited.put(p, current);

            for (Position newPos : p.getNeighborsInBounds()){
                if(this.lines.get(newPos.getY()).charAt(newPos.getX()) == '#')
                    continue;

                if(visited.containsKey(newPos)){
                    continue;
                }

                queue.add(new PositionState(newPos, current.currentSteps+1));
            }
        }

        System.out.println(cheats);
        long result = 0;

        for (int k : cheats.keySet()){
            result += cheats.get(k);
        }

        System.out.println("Solution Stage 2: " + result);
    }
}