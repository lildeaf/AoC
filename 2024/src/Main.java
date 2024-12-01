public class Main {
    public static void main(String[] args) {
        assert args.length == 2 : "Wrong Arguments";
        Day day = null;
        switch (Integer.parseInt(args[1])){
            case 1 -> day = new Day01(Boolean.parseBoolean(args[0]));
            default -> {
                System.out.println("Second argument must be a number between 1 and 25");
                System.exit(-1);
            }
        }
        day.solveStage1();
        day.solveStage2();
    }
}
