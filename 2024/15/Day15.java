import java.util.*;

public class Day15 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private ArrayList<String> map;
    private HashSet<Position> boxes;
    private Position robot;

    private HashMap<Position, Position> dualBoxes;

    private static final String DAY = "15";

    public Day15(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private void printMap(char move){
        System.out.println("Move " + move);
        //for (Position k : this.boxes.keySet()){
        //    System.out.println(k + " HASH: " +k.hashCode());
        //}

        for (int y = 0; y < this.map.size(); y++){
            String l = this.map.get(y);
            for (int x = 0; x < l.length(); x++){
                if (l.charAt(x) == '#'){
                    System.out.print('#');
                    continue;
                }

                if (robot.getX() == x && robot.getY() == y){
                    System.out.print('@');
                    continue;
                }

                if (this.boxes.contains(new Position(x, y, this.map)))
                    System.out.print('O');
                else
                    System.out.print('.');
            }
            System.out.println();
        }
    }

    private void printMap2(char move){
        System.out.println("Move " + move);

        for (int y = 0; y < this.map.size(); y++){
            String l = this.map.get(y);
            for (int x = 0; x < l.length(); x++){
                if (l.charAt(x) == '#'){
                    System.out.print('#');
                    continue;
                }

                if (robot.getX() == x && robot.getY() == y){
                    System.out.print('@');
                    continue;
                }

                if (this.dualBoxes.containsKey(new Position(x, y, this.map)))
                    System.out.print('O');
                else
                    System.out.print('.');
            }
            System.out.println();
        }
    }


    private void attemptMove(int direction){
        HashMap<Position, Position> movedBoxes = new HashMap<>();

        Position current = robot;
        HashSet<Position> newBoxes = new HashSet<>();

        current.move(direction);
        //moved.push(current);

        while(true){
            if(this.map.get(current.getY()).charAt(current.getX()) == '#'){
                robot.move((direction + 2) % 4);
                return;
            }

            if(!this.boxes.contains(current)){
                break;
            }

            //add to Boxes to be moved
            Position movedBox = new Position(current, this.map);
            movedBox.move(direction);

            movedBoxes.put(current, movedBox);
            current = movedBox;
        }

        for (Position p : this.boxes){
            newBoxes.add(movedBoxes.getOrDefault(p, p));
        }

        this.boxes = newBoxes;
    }

    private void attemptMoveStage2(int direction){
        HashMap<Position, Position> movedBoxes = new HashMap<>();

        Queue<Position> movingObjects = new LinkedList<>();

        Position current;
        HashSet<Position> newBoxes = new HashSet<>();
        HashMap<Position, Position> newDualBoxes = new HashMap<>();

        robot.move(direction);
        movingObjects.add(robot);

        while(!movingObjects.isEmpty()){
            current = movingObjects.remove();

            if(this.map.get(current.getY()).charAt(current.getX()) == '#'){
                robot.move((direction + 2) % 4);
                return;
            }

            if(!this.dualBoxes.containsKey(current)){
                continue;
            }

            //add to Boxes to be moved
            Position movedBox1 = new Position(current, this.map);
            Position prevDual = this.dualBoxes.get(movedBox1);
            Position movedBox2 = new Position(prevDual, this.map);

            movedBox1.move(direction);
            movedBox2.move(direction);

            movedBoxes.put(current, movedBox1);
            movedBoxes.put(prevDual, movedBox2);
            newDualBoxes.put(movedBox1, movedBox2);
            newDualBoxes.put(movedBox2, movedBox1);

            if(direction % 2 == 0)
                movingObjects.add(movedBox1);
            movingObjects.add(movedBox2);
        }

        for (Position p : movedBoxes.keySet()){
            this.dualBoxes.remove(p);
        }

        for (Position p : movedBoxes.keySet()){
            Position newP = movedBoxes.get(p);
            Position dual = newDualBoxes.get(newP);

            this.dualBoxes.put(newP, dual);
            this.dualBoxes.put(dual, newP);
        }
    }

    private int init(){
        this.map = new ArrayList<>();
        this.boxes = new HashSet<>();
        this.robot = new Position(this.map);

        int y = 0;
        while(this.lines.get(y).length() != 0){
            String line = this.lines.get(y);
            map.add(line);
            for (int x = 0; x < line.length(); x++){
                char c = line.charAt(x);
                if (c == '@'){
                    robot.setX(x);
                    robot.setY(y);
                }
                if (c == 'O'){
                    Position box = new Position(x,y, this.map);
                    boxes.add(box);
                }
            }
            y++;
        }

        return ++y;
    }

    private int initStage2(){
        this.map = new ArrayList<>();
        this.robot = new Position(this.map);
        this.dualBoxes = new HashMap<>();

        int y = 0;
        while(this.lines.get(y).length() != 0){
            String line = this.lines.get(y);
            StringBuilder slice = new StringBuilder();
            for (int x = 0; x < line.length(); x++){
                char c = line.charAt(x);
                switch (c){
                    case '#' -> slice.append("##");
                    case '.' -> slice.append("..");
                    case '@' -> {
                        robot.setX(slice.length());
                        robot.setY(y);
                        slice.append("@.");
                    }
                    case 'O' -> {
                        Position box1 = new Position(slice.length(),y, this.map);
                        Position box2 = new Position(slice.length()+1,y, this.map);
                        this.dualBoxes.put(box1, box2);
                        this.dualBoxes.put(box2, box1);
                        slice.append("[]");
                    }
                }
            }
            this.map.add(slice.toString());
            y++;
        }

        return ++y;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;
        int y = init();

        for (; y < this.lines.size(); y++){
            String directions = this.lines.get(y);
            for(int i = 0; i < directions.length(); i++){
                int direction = -1;
                switch (directions.charAt(i)){
                    case '^' -> direction = 0;
                    case '>' -> direction = 1;
                    case 'v' -> direction = 2;
                    case '<' -> direction = 3;
                    default -> System.exit(direction);
                }

                attemptMove(direction);
            }
        }

        for (Position box : this.boxes){
            sum += box.getY()*100 + box.getX();
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int sum = 0;
        int y = initStage2();

        for (; y < this.lines.size(); y++){
            String directions = this.lines.get(y);
            for(int i = 0; i < directions.length(); i++){
                int direction = -1;
                switch (directions.charAt(i)){
                    case '^' -> direction = 0;
                    case '>' -> direction = 1;
                    case 'v' -> direction = 2;
                    case '<' -> direction = 3;
                    default -> System.exit(direction);
                }

                attemptMoveStage2(direction);
            }
        }

        Set<Position> alreadyCounted = new HashSet<>();

        for (Position box : dualBoxes.keySet()){
            if (alreadyCounted.contains(box))
                continue;
            Position box2 = dualBoxes.get(box);
            sum +=  box.getY()*100 + Math.min(box.getX(), box2.getX());

            alreadyCounted.add(box2);
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
