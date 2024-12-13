import java.math.BigInteger;
import java.util.ArrayList;

public class Day13 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "13";

    public Day13(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private Position getPosition(String line, String delimiter){
        Position button = new Position();
        String[] vals = line.split(", ");

        button.setX(Integer.parseInt(vals[0].split(delimiter)[1]));
        button.setY(Integer.parseInt(vals[1].split(delimiter)[1]));

        return button;
    }

    private int minTokens(Position buttonA, Position buttonB, Position prize){
        int countA = 0;
        int aX = buttonA.getX();
        int aY = buttonA.getY();

        int bX = buttonB.getX();
        int bY = buttonB.getY();
        do {
            int prizeX = prize.getX();
            int prizeY = prize.getY();

            if(prizeX % bX == 0 && prizeY % bY == 0 && (prizeX/bX) == (prizeY/bY))
            {
                int countB = prizeX /bX;
                if((countA <= 100 && countB <= 100))
                    return countB + countA*3;
            }

            countA++;
            prize.updateX(-aX);
            prize.updateY(-aY);
        }while(prize.getX() > 0 && prize.getY() > 0);

        return 0;
    }

    private BigInteger minTokensStage2(Position buttonA, Position buttonB, long prizeX, long prizeY){
        double aX = buttonA.getX();
        double aY = buttonA.getY();

        double bX = buttonB.getX();
        double bY = buttonB.getY();

        double invMult = 1 / (aX * bY - aY * bX);
        aX *= invMult;
        aY *= invMult * (-1);
        bX *= invMult * (-1);
        bY *= invMult;

        BigInteger countA = new BigInteger(String.valueOf(Math.round(bY * prizeX + bX * prizeY)));
        BigInteger countB = new BigInteger(String.valueOf(Math.round(aY * prizeX + aX * prizeY)));

        BigInteger resX = countA.multiply(new BigInteger(String.valueOf(buttonA.getX()))).add(countB.multiply(new BigInteger(String.valueOf(buttonB.getX()))));
        BigInteger resY = countA.multiply(new BigInteger(String.valueOf(buttonA.getY()))).add(countB.multiply(new BigInteger(String.valueOf(buttonB.getY()))));

        if(Long.parseUnsignedLong(resX.toString()) == prizeX && Long.parseUnsignedLong(resY.toString()) == prizeY){
            return new BigInteger("3").multiply(new BigInteger(String.valueOf(countA))).add(new BigInteger(String.valueOf(countB)));
        }

        return BigInteger.ZERO;
    }


    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int sum = 0;

        for(int i = 0; i < this.lines.size(); i+=4){
            Position buttonA = getPosition(this.lines.get(i).substring(10), "\\+");
            Position buttonB = getPosition(this.lines.get(i+1).substring(10), "\\+");
            Position prize = getPosition(this.lines.get(i+2).substring(7), "=");

            int res = minTokens(buttonA, buttonB, prize);
            sum += res;

        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        BigInteger sum = BigInteger.ZERO;

        for(int i = 0; i < this.lines.size(); i+=4){
            Position buttonA = getPosition(this.lines.get(i).substring(10), "\\+");
            Position buttonB = getPosition(this.lines.get(i+1).substring(10), "\\+");
            Position prize = getPosition(this.lines.get(i+2).substring(7), "=");

            long prizeX =  Long.parseUnsignedLong("10000000000000") + (long)prize.getX();
            long prizeY =  Long.parseUnsignedLong("10000000000000") + (long)prize.getY();

            BigInteger res = minTokensStage2(buttonA, buttonB, prizeX, prizeY);
            sum = sum.add(res);
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
