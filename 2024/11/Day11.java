import java.math.BigInteger;
import java.util.*;

public class Day11 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "11";

    private final Map<Long, Map<Integer, Integer>> cache = new HashMap<>();
    private final Map<BigInteger, Map<Integer, BigInteger>> cache2 = new HashMap<>();
    private static final BigInteger multiplier = new BigInteger("2024");

    public Day11(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private int blink(long stone, int time){
        if(time == 0){
            return 1;
        }

        Map<Integer, Integer> stoneCache = cache.getOrDefault(stone, new HashMap<>());
        if(stoneCache.containsKey(time))
            return stoneCache.get(time);

        if(stone == 0){
            int res = blink(1, time-1);
            stoneCache.put(time, res);
            cache.put(stone, stoneCache);
            return res;
        }

        int digits = (int) (Math.floor(Math.log10(stone)) + 1);
        if(digits % 2 == 1){
            int res = blink( stone * 2024, time-1);
            stoneCache.put(time, res);
            cache.put(stone, stoneCache);
            return res;
        }

        assert stone > 0;
        String num = String.valueOf(stone);

        long num1 = Long.parseLong(num.substring(0, num.length()/2));
        long num2 = Long.parseLong(num.substring(num.length()/2));
        int res = blink(num1, time-1) + blink(num2, time-1);
        stoneCache.put(time, res);
        cache.put(stone, stoneCache);
        return res;
    }

    private BigInteger blink2(BigInteger stone, int time){
        if(time == 0){
            return BigInteger.ONE;
        }

        Map<Integer, BigInteger> stoneCache = cache2.getOrDefault(stone, new HashMap<>());
        if(stoneCache.containsKey(time))
            return stoneCache.get(time);

        if(stone.compareTo(BigInteger.ZERO) == 0){
            BigInteger res = blink2(BigInteger.ONE, time-1);
            stoneCache.put(time, res);
            cache2.put(stone, stoneCache);
            return res;
        }

        int digits = stone.toString().length();
        if(digits % 2 == 1){
            BigInteger res = blink2(stone.multiply(multiplier), time-1);
            stoneCache.put(time, res);
            cache2.put(stone, stoneCache);
            return res;
        }

        String num = String.valueOf(stone);

        BigInteger num1 = new BigInteger(num.substring(0, num.length()/2));
        BigInteger num2 = new BigInteger(num.substring(num.length()/2));
        BigInteger res = blink2(num1, time-1).add(blink2(num2, time-1));
        stoneCache.put(time, res);
        cache2.put(stone, stoneCache);
        return res;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");

        List<Long> stones = Arrays.stream(this.lines.getFirst().split(" ")).map(Long::valueOf).toList();

        int sum = 0;
        for(Long stone: stones){
            sum += blink(stone, 25);
        }

        System.out.println("Solution Stage 1: " + sum);
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        cache.clear();
        String[] stones = this.lines.getFirst().split(" ");

        BigInteger sum = BigInteger.ZERO;
        for(String stone: stones){
            sum = sum.add(blink2(new BigInteger(stone), 75));
        }

        System.out.println("Solution Stage 2: " + sum);
    }
}