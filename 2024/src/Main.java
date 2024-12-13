public class Main {
    public static void main(String[] args) {
        assert args.length == 2 : "Wrong Arguments";
        Day day = null;
        switch (Integer.parseInt(args[1])){
            case 1 -> day = new Day01(Boolean.parseBoolean(args[0]));
            case 2 -> day = new Day02(Boolean.parseBoolean(args[0]));
            case 3 -> day = new Day03(Boolean.parseBoolean(args[0]));
            case 4 -> day = new Day04(Boolean.parseBoolean(args[0]));
            case 5 -> day = new Day05(Boolean.parseBoolean(args[0]));
            case 6 -> day = new Day06(Boolean.parseBoolean(args[0]));
            case 7 -> day = new Day07(Boolean.parseBoolean(args[0]));
            case 8 -> day = new Day08(Boolean.parseBoolean(args[0]));
            case 9 -> day = new Day09(Boolean.parseBoolean(args[0]));
            case 10 -> day = new Day10(Boolean.parseBoolean(args[0]));
            case 11 -> day = new Day11(Boolean.parseBoolean(args[0]));
            case 12 -> day = new Day12(Boolean.parseBoolean(args[0]));
            case 13 -> day = new Day13(Boolean.parseBoolean(args[0]));
            case 14 -> day = new Day14(Boolean.parseBoolean(args[0]));
            case 15 -> day = new Day15(Boolean.parseBoolean(args[0]));
            case 16 -> day = new Day16(Boolean.parseBoolean(args[0]));
            case 17 -> day = new Day17(Boolean.parseBoolean(args[0]));
            case 18 -> day = new Day18(Boolean.parseBoolean(args[0]));
            case 19 -> day = new Day19(Boolean.parseBoolean(args[0]));
            case 20 -> day = new Day20(Boolean.parseBoolean(args[0]));
            case 21 -> day = new Day21(Boolean.parseBoolean(args[0]));
            case 22 -> day = new Day22(Boolean.parseBoolean(args[0]));
            case 23 -> day = new Day23(Boolean.parseBoolean(args[0]));
            case 24 -> day = new Day24(Boolean.parseBoolean(args[0]));
            case 25 -> day = new Day25(Boolean.parseBoolean(args[0]));
            default -> {
                System.out.println("Second argument must be a number between 1 and 25"); 
                System.exit(-1);
            }
        }
        long startTime = System.currentTimeMillis();
        day.solveStage1();
        long endTime = System.currentTimeMillis();
        System.out.println("Stage 1 took: " + (endTime - startTime)/1000f + "s");
        System.out.println();
        startTime = System.currentTimeMillis();
        day.solveStage2();
        endTime = System.currentTimeMillis();
        System.out.println("Stage 2 took: " + (endTime - startTime)/1000f + "s");
    }
}
