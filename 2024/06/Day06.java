import java.util.*;

public class Day06 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "06";

    public Day06(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");

        int x = 0, y = 0;
        for(; y < this.lines.size(); y++){
            boolean found = false;
            x = 0;
            for(; x < this.lines.get(y).length(); x++){
                char c = this.lines.get(y).charAt(x);
                if(c != '.' && c != '#') {
                    found = true;
                    break;
                }
            }
            if (found)
                break;
        }

        Position pos = new Position(x, y, this.lines);
        Set<Position> visited = new HashSet<>();
        int direction = 0; //0 = up, 1 = r, 2 = d, 3 = l
        while(true){
            visited.add(pos);
            Position nextPos = new Position(pos.getX(), pos.getY(), this.lines);
            nextPos.move(direction);

            if(nextPos.outOfBounds())
                break;

            char nextC = this.lines.get(nextPos.getY()).charAt(nextPos.getX());
            if(nextC == '#'){
                direction = (direction+1)%4;
                pos = new Position(pos.getX(), pos.getY(), this.lines);
            }else {
                pos = nextPos;
            }
        }

        System.out.println("Solving Stage 1..." + visited.size());
    }

    private boolean checkDir(Position pos, int direction, Position newObstacle){
        Position current = new Position(pos.getX(), pos.getY(), this.lines);
        int currentDir = direction;
        HashMap<Position, Set<Integer>> visited = new HashMap<>();

        while(true){
            Set<Integer> d = visited.getOrDefault(current, new HashSet<>());
            if(d.contains(currentDir)){
                return true;
            }
            d.add(currentDir);
            visited.put(current, d);

            Position nextPos = new Position(current.getX(), current.getY(), this.lines);
            nextPos.move(currentDir);

            if(nextPos.outOfBounds())
                break;

            char nextC = this.lines.get(nextPos.getY()).charAt(nextPos.getX());
            if(nextC == '#' || newObstacle.equals(nextPos)){
                currentDir = (currentDir+1)%4;
            }else {
                current = nextPos;
            }
        }

        return false;
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");

        int x = 0,y = 0;
        for(; y < this.lines.size(); y++){
            boolean found = false;
            x = 0;
            for(; x < this.lines.get(y).length(); x++){
                char c = this.lines.get(y).charAt(x);
                if(c != '.' && c != '#') {
                    found = true;
                    break;
                }
            }
            if (found)
                break;
        }

        Position pos = new Position(x, y, this.lines);
        HashMap<Position, Set<Integer>> positionsWithDirections = new HashMap<>();
        Set<Position> obstacles = new HashSet<>();
        Set<Position> checked = new HashSet<>();


        int direction = 0; //0 = up, 1 = r, 2 = d, 3 = l
        while(true){
            Set<Integer> s = positionsWithDirections.getOrDefault(pos, new HashSet<>());
            s.add(direction);
            positionsWithDirections.put(pos, s);

            Position nextPos = new Position(pos.getX(), pos.getY(), this.lines);
            nextPos.move(direction);

            if(nextPos.outOfBounds())
                break;

            char nextC = this.lines.get(nextPos.getY()).charAt(nextPos.getX());
            if(nextC == '#'){
                direction = (direction+1)%4;
                pos = new Position(pos.getX(), pos.getY(), this.lines);
            }else {
                if(!checked.contains(nextPos) &&
                        nextC == '.' &&
                        checkDir(pos, (direction+1)%4, nextPos)){
                    obstacles.add(nextPos);
                }
                checked.add(nextPos);

                pos = nextPos;
            }
        }


        System.out.println("Solution Stage 2: " + obstacles.size());
    }
}