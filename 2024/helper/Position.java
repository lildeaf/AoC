import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Position {
    private int x;
    private int y;

    private ArrayList<String> map;

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public void updateX(int x){
        this.x += x;
    }
    public void updateY(int y){
        this.y += y;
    }

    public Position(ArrayList<String> map) {
        this.x = 0;
        this.y = 0;

        this.map = map;
    }

    public Position(int x, int y, ArrayList<String> map) {
        this.x = x;
        this.y = y;

        this.map = map;
    }

    public Position(Position pos, ArrayList<String> map) {
        this.x = pos.getX();
        this.y = pos.getY();
        this.map = map;
    }

    public boolean outOfBounds() {
        return this.y < 0 || this.x < 0 || this.y >= map.size() || this.x >= map.get(this.y).length();
    }

    public Set<Position> getNeighborsInBounds(){
        Set<Position> neighbors = new HashSet<>();
        int maxY = map.size();
        int maxX = map.getFirst().length();

        if(this.y - 1 >= 0)
            neighbors.add(new Position(this.x, this.y - 1, this.map));
        if(this.y + 1 < maxY)
            neighbors.add(new Position(this.x, this.y + 1, this.map));
        if(this.x - 1 >= 0)
            neighbors.add(new Position(this.x - 1, this.y, this.map));
        if(this.x + 1 < maxX)
            neighbors.add(new Position(this.x + 1, this.y, this.map));

        return neighbors;
    }

    public Set<Position> getAllNeighbors(){
        Set<Position> neighbors = new HashSet<>();

        neighbors.add(new Position(this.x, this.y - 1, this.map));
        neighbors.add(new Position(this.x, this.y + 1, this.map));
        neighbors.add(new Position(this.x - 1, this.y, this.map));
        neighbors.add(new Position(this.x + 1, this.y, this.map));

        return neighbors;
    }

    public void move(int direction){
        switch (direction){
            case 0 -> this.y--;
            case 1 -> this.x++;
            case 2 -> this.y++;
            case 3 -> this.x--;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;
        Position that = (Position) o;
        return x == that.x && y == that.y;
    }

    @Override
    public int hashCode() {
        return y * this.map.getFirst().length() + x;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
}
