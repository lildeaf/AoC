import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class Day08 implements Day {
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "08";

    public Day08(boolean testing) {
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if (this.lines == null) {
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        HashMap<Character, ArrayList<Position>> antennas = new HashMap<>();
        Set<Position> antinodes = new HashSet<>();

        for (int y = 0; y < this.lines.size(); y++) {
            String line = this.lines.get(y);
            for (int x = 0; x < line.length(); x++) {
                Character c = line.charAt(x);
                if (c == '.')
                    continue;

                Position newAntenna = new Position(x, y, this.lines);
                ArrayList<Position> positions = antennas.getOrDefault(c, new ArrayList<>());

                for (Position p : positions) {
                    Position diff = new Position(p.getX() - newAntenna.getX(), p.getY() - newAntenna.getY(), this.lines);
                    Position one = new Position(p.getX() + diff.getX(), p.getY() + diff.getY(), this.lines);
                    Position two = new Position(newAntenna.getX() - diff.getX(), newAntenna.getY() - diff.getY(), this.lines);

                    if (!one.outOfBounds())
                        antinodes.add(one);
                    if (!two.outOfBounds())
                        antinodes.add(two);
                }

                positions.add(newAntenna);
                antennas.put(c, positions);
            }
        }

        System.out.println("Solution Stage 1 : " + antinodes.size());
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        HashMap<Character, ArrayList<Position>> antennas = new HashMap<>();
        Set<Position> antinodes = new HashSet<>();

        for (int y = 0; y < this.lines.size(); y++) {
            String line = this.lines.get(y);
            for (int x = 0; x < line.length(); x++) {
                Character c = line.charAt(x);
                if (c == '.')
                    continue;

                Position newAntenna = new Position(x, y, this.lines);
                ArrayList<Position> positions = antennas.getOrDefault(c, new ArrayList<>());

                for (Position p : positions) {
                    Position diff = new Position(p.getX() - newAntenna.getX(), p.getY() - newAntenna.getY(), this.lines);
                    Position ant = new Position(p, this.lines);
                    while(!ant.outOfBounds()){
                        antinodes.add(new Position(ant, this.lines));
                        ant = new Position(ant.getX() + diff.getX(), ant.getY() + diff.getY(), this.lines);
                    }

                    ant = new Position(newAntenna, this.lines);
                    while(!ant.outOfBounds()){
                        antinodes.add(new Position(ant, this.lines));
                        ant = new Position(ant.getX() - diff.getX(), ant.getY() - diff.getY(), this.lines);
                    }
                }

                positions.add(newAntenna);
                antennas.put(c, positions);
            }
        }

        System.out.println("Solution Stage 2: " + antinodes.size());
    }
}