import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;

public class Day22 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "22";

    private BigInteger sixtyFour = new BigInteger("64");
    private BigInteger thirtyTwo = new BigInteger("32");
    private BigInteger twoThousand = new BigInteger("2048");
    private BigInteger pruneValue = new BigInteger("16777216");

    private HashMap<BigInteger, BigInteger> cache = new HashMap<>();

    public Day22(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private BigInteger mix(BigInteger secret, BigInteger number){
        return secret.xor(number);
    }

    private BigInteger prune(BigInteger secret){
        return secret.mod(this.pruneValue);
    }

    private BigInteger calcNext(BigInteger secret)
    {
        BigInteger mult = secret.multiply(this.sixtyFour);
        BigInteger newSecret = mix(secret, mult);
        newSecret = prune(newSecret);

        BigInteger div = newSecret.divide(thirtyTwo);
        newSecret = mix(newSecret, div);
        newSecret = prune(newSecret);

        mult = newSecret.multiply(this.twoThousand);
        newSecret = mix(newSecret, mult);
        newSecret = prune(newSecret);

        return newSecret;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        ArrayList<BigInteger> monkeys = new ArrayList<>();
        for (String line : this.lines){
            monkeys.add(new BigInteger(line));
        }

        for(int i = 0; i < 2000; i++){
            for (int j = 0; j < monkeys.size(); j++){
                BigInteger secret = monkeys.get(j);
                secret = calcNext(secret);
                monkeys.set(j, secret);
            }
        }

        BigInteger sum = BigInteger.ZERO;
        for (BigInteger s : monkeys){
            sum = sum.add(s);
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        ArrayList<BigInteger> monkeys = new ArrayList<>();
        for (String line : this.lines){
            monkeys.add(new BigInteger(line));
        }

        HashMap<String, BigInteger> sequences = new HashMap<>();
        BigInteger ten = new BigInteger("10");
        for (int j = 0; j < monkeys.size(); j++){
            HashSet<String> sequencesSeen = new HashSet<>();
            Stack<Integer> stack = new Stack<>();
            for(int i = 0; i < 2000; i++){
                BigInteger secret = monkeys.get(j);
                BigInteger newSecret = calcNext(secret);
                monkeys.set(j, newSecret);

                BigInteger oneValue = newSecret.mod(ten);
                BigInteger diff = oneValue.subtract(secret.mod(ten));
                stack.push(diff.intValue());
                if(i < 3)
                    continue;

                int val1 = stack.pop();
                int val2 = stack.pop();
                int val3 = stack.pop();
                int val4 = stack.pop();
                stack.push(val4);
                stack.push(val3);
                stack.push(val2);
                stack.push(val1);

                String k = String.valueOf(val1) + String.valueOf(val2) + String.valueOf(val3) + String.valueOf(val4);

                if (sequencesSeen.contains(k))
                    continue;

                sequencesSeen.add(k);
                BigInteger current = sequences.getOrDefault(k, BigInteger.ZERO);
                sequences.put(k, current.add(oneValue));
            }
        }
        BigInteger sum = BigInteger.ZERO;
        for (String k : sequences.keySet()){
            BigInteger val = sequences.get(k);
            if (sum.compareTo(val) < 0)
                sum = val;
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}
