import java.util.*;

public class Day16 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "16";

    public Day16(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private class PositionState {
        Position p;
        int direction;
        int currentScore;

        Set<Position> positions;

        public PositionState(Position p, int dir, int score){
            this.p = p;
            this.direction = dir;
            this.currentScore = score;

            positions = new HashSet<>();
            positions.add(p);
        }

        public void addMultiplePos(Set<Position> p){
            positions.addAll(p);
        }

        @Override
        public String toString() {
            return p.toString() + ", " + direction + ", " + currentScore;
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int result = 0;

        Position end = new Position(this.lines.getFirst().length()-2, 1, this.lines);
        Position start = new Position(1, this.lines.size()-2, this.lines);

        Set<Position> visited = new HashSet<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentScore));
        queue.add(new PositionState(start, 1, 0));

        System.out.println(start);
        System.out.println(end);
        while (true){
            PositionState current = queue.poll();
            if(current.p.equals(end)){
                result = current.currentScore;
                break;
            }

            Position p = current.p;
            visited.add(p);

            int currentDir = current.direction;
            for(int d = 0; d < 4; d++){
                Position newPos = new Position(p, this.lines);
                newPos.move(d);
                if(visited.contains(newPos)){
                    continue;
                }

                if(this.lines.get(newPos.getY()).charAt(newPos.getX()) == '#')
                    continue;

                if(d == currentDir){
                    queue.add(new PositionState(newPos, d, current.currentScore+1));
                }

                if(Math.abs(d-currentDir) % 2 == 1){
                    queue.add(new PositionState(newPos, d, current.currentScore+1001));
                }
            }
        }

        System.out.println("Solution Stage 1: " + result);
    }

    private void printMapWithPaths(Set<Position> visited){
        for (int y = 0; y < this.lines.size(); y++){
            String line = this.lines.get(y);
            for (int x = 0; x < line.length(); x++){
                char c = line.charAt(x);
                if(c == '#')
                    System.out.print(c);
                else
                    System.out.print(visited.contains(new Position(x,y, this.lines)) ? 'O' : c);
            }
            System.out.println();
        }
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int result = 0;

        Position end = new Position(this.lines.getFirst().length()-2, 1, this.lines);
        Position start = new Position(1, this.lines.size()-2, this.lines);

        HashMap<Position, PositionState> visited = new HashMap<>();
        PriorityQueue<PositionState> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.currentScore));
        queue.add(new PositionState(start, 1, 0));

        System.out.println(start);
        System.out.println(end);
        while (true){
            PositionState current = queue.poll();
            if(current.p.equals(end)){
                //printMapWithPaths(current.positions);
                result = current.positions.size();
                break;
            }

            Position p = current.p;
            if(visited.containsKey(p)){
                if (visited.get(p).currentScore+1000 < current.currentScore)
                    continue;
            }

            PositionState vis = visited.getOrDefault(p, new PositionState(current.p, current.direction, current.currentScore));
            vis.addMultiplePos(current.positions);
            visited.put(p, vis);

            int currentDir = current.direction;
            for(int d = 0; d < 4; d++){
                Position newPos = new Position(p, this.lines);
                newPos.move(d);

                if(this.lines.get(newPos.getY()).charAt(newPos.getX()) == '#')
                    continue;

                PositionState state = new PositionState(newPos, d, current.currentScore+1);
                state.addMultiplePos(vis.positions);
                if(d == currentDir){
                    queue.add(state);
                    continue;
                }

                if(Math.abs(d-currentDir) % 2 == 1){
                    state.currentScore += 1000;

                    queue.add(state);
                }
            }
        }

        System.out.println("Solution Stage 2: " + result);
    }
}
