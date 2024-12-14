import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.awt.image.WritableRaster;
import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Day14 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "14";

    private int spaceX;
    private int spaceY;

    public Day14(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }

        this.spaceX = testing ? 11 : 101;
        this.spaceY = testing ? 7 : 103;
    }

    private void printToFile(HashSet<Position> robots, String fileName){
        BufferedImage b = new BufferedImage(this.spaceX, this.spaceY, BufferedImage.TYPE_BYTE_GRAY);
        WritableRaster raster = b.getRaster();
        for (int y = 0; y < this.spaceY; y++){
            for (int x = 0; x < this.spaceX; x++){
                if(robots.contains(new Position(x,y)))
                    raster.setSample(x,y,0, 255);
            }
        }
        try {
            ImageIO.write(b, "png", new File(fileName));
        } catch (Exception e){
            e.printStackTrace();
        }
    }

    private static class Robot{
        Position p;
        Position v;

        public Position getPosition() {
            return p;
        }

        public Position getVelocity() {
            return v;
        }

        public void setPosition(Position p) {
            this.p = p;
        }

        public void setVelocity(Position v) {
            this.v = v;
        }

        public Robot(){
            this.p = new Position();
            this.v = new Position();
        }

        public void move(int seconds, int spaceX, int spaceY){
            int newX = Math.floorMod(seconds * v.getX() + p.getX(), spaceX);
            int newY = Math.floorMod(seconds * v.getY() + p.getY(), spaceY);

            p.setX(newX);
            p.setY(newY);
        }

        public int getQuadrant(int spaceX, int spaceY){
            int xDiv = spaceX/2, yDiv = spaceY/2;
            if(p.getX() == xDiv || p.getY() == yDiv)
                return -1;
            int xHalf = 0, yHalf = 0;
            if(p.getX() > xDiv)
                xHalf = 1;
            if(p.getY() > yDiv)
                yHalf = 2;

            return xHalf + yHalf;
        }

        @Override
        public String toString() {
            return "ROBOT{" + this.p + ", " + this.v + "}";
        }
    }

    private Position getPosition(String line){
        Position p = new Position();

        String[] coords = line.split(",");
        p.setX(Integer.parseInt(coords[0]));
        p.setY(Integer.parseInt(coords[1]));

        return p;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int result = 0;

        ArrayList<Robot> robots = new ArrayList<>();

        for(String line : this.lines){
            Robot robot = new Robot();
            String[] robotLine = line.split(" ");
            robot.setPosition(getPosition(robotLine[0].substring(2)));
            robot.setVelocity(getPosition(robotLine[1].substring(2)));

            robots.add(robot);
        }

        HashMap<Integer, Integer> quadrantCount = new HashMap<>();
        quadrantCount.put(0,0);
        quadrantCount.put(1,0);
        quadrantCount.put(2,0);
        quadrantCount.put(3,0);

        for (Robot robot : robots){
            robot.move(100, this.spaceX, this.spaceY);
            int quadrant = robot.getQuadrant(this.spaceX, this.spaceY);
            if(quadrant == -1)
                continue;
            quadrantCount.compute(quadrant, (k, v) -> v+1);
        }

        System.out.println(quadrantCount);
        result = quadrantCount.get(0) * quadrantCount.get(1) *
                quadrantCount.get(2) * quadrantCount.get(3);

        System.out.println("Solution Stage 1: " + result);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");

        ArrayList<Robot> robots = new ArrayList<>();

        for(String line : this.lines){
            Robot robot = new Robot();
            String[] robotLine = line.split(" ");
            robot.setPosition(getPosition(robotLine[0].substring(2)));
            robot.setVelocity(getPosition(robotLine[1].substring(2)));

            robots.add(robot);
        }

        String outDir = "14"+ System.getProperty("file.separator") + "outFiles"+ System.getProperty("file.separator");
        for (int i= 0; i < this.spaceX*this.spaceY; i++){
            HashSet<Position> robotPositions = new HashSet<>(robots.stream().map(Robot::getPosition).toList());
            printToFile(robotPositions, outDir + "time" + i + ".png");

            for (Robot r : robots)
                r.move(1, this.spaceX, this.spaceY);
        }

        System.out.println("Solution Stage 2: check outFiles folder");
    }
}