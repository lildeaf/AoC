import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class Day17 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "17";

    public Day17(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private static class Computer{
        BigInteger registerA;
        BigInteger registerB;
        BigInteger registerC;

        ArrayList<Integer> instructions;
        String instructionString;
        int instrPointer;

        HashMap<Integer, BigInteger> literals = new HashMap<>();

        public Computer(BigInteger a, BigInteger b, BigInteger c, ArrayList<Integer> instructions){
            this.registerA = a;
            this.registerB = b;
            this.registerC = c;

            this.instructions = instructions;
            this.instructionString = this.instructions.stream().map(String::valueOf).collect(Collectors.joining(","));
            this.instrPointer = 0;

            for (int i = 0; i < 9; i++)
                literals.put(i, new BigInteger(String.valueOf(i)));
        }

        public void div(int resultRegister, BigInteger value){
            BigInteger denom = BigInteger.TWO.pow(value.intValue());
            BigInteger result = this.registerA.divide(denom);
            switch (resultRegister){
                case 0 -> this.registerA = result;
                case 1 -> this.registerB = result;
                case 2 -> this.registerC = result;
            }
        }

        public void bXor(BigInteger value){
            this.registerB = this.registerB.xor(value);
        }

        public void bSt(BigInteger value){
            this.registerB = value.mod(literals.get(8));
        }

        public String out(BigInteger value){
            return value.mod(literals.get(8)).toString();
        }

        private BigInteger getCombo(int combo){
            BigInteger value = BigInteger.ZERO;
            switch (combo){
                case 0 -> value = BigInteger.ZERO;
                case 1 -> value = BigInteger.ONE;
                case 2 -> value = BigInteger.TWO;
                case 3 -> value = literals.get(3);
                case 4 -> value = this.registerA;
                case 5 -> value = this.registerB;
                case 6 -> value = this.registerC;
            }

            return value;
        }

        public String run(){
            this.instrPointer = 0;
            ArrayList<String> outs = new ArrayList<>();

            while(instrPointer < this.instructions.size()){
                switch (this.instructions.get(instrPointer)){
                    case 0 -> div(0, getCombo(this.instructions.get(instrPointer+1)));
                    case 1 -> bXor(literals.get(this.instructions.get(instrPointer+1)));
                    case 2 -> bSt(getCombo(this.instructions.get(instrPointer+1)));
                    case 3 -> this.instrPointer = this.registerA.compareTo(BigInteger.ZERO) != 0 ? this.instructions.get(instrPointer+1)-2 : this.instrPointer;
                    case 4 -> bXor(this.registerC);
                    case 5 -> outs.add(out(getCombo(this.instructions.get(instrPointer+1))));
                    case 6 -> div(1, getCombo(this.instructions.get(instrPointer+1)));
                    case 7 -> div(2, getCombo(this.instructions.get(instrPointer+1)));
                    default -> System.exit(-1);
                }

                instrPointer += 2;
            }

            return String.join(",", outs);
        }

        @Override
        public String toString() {
            return "{" + this.registerA + ", " + this.registerB + ", " + this.registerC + ", " + this.instrPointer + "}";
        }
    }

    private BigInteger parseRegister(String line){
        return new BigInteger(line.split(": ")[1]);
    }

    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        BigInteger a = parseRegister(this.lines.get(0));
        BigInteger b = parseRegister(this.lines.get(1));
        BigInteger c = parseRegister(this.lines.get(2));

        String[] instr = this.lines.get(4).split(": ")[1].split(",");
        ArrayList<Integer> instructions = new ArrayList<Integer>(Arrays.stream(instr).mapToInt(Integer::parseInt).boxed().toList());

        Computer comp = new Computer(a,b, c, instructions);
        String res = comp.run();

        System.out.println("Solution Stage 1: " + res);


    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        BigInteger a = BigInteger.ZERO;
        BigInteger b = parseRegister(this.lines.get(1));
        BigInteger c = parseRegister(this.lines.get(2));

        String[] instr = this.lines.get(4).split(": ")[1].split(",");
        ArrayList<Integer> instructions = new ArrayList<>(Arrays.stream(instr).mapToInt(Integer::parseInt).boxed().toList());
        Computer comp = new Computer(a, b, c, instructions);
        List<String> i = new ArrayList<>(List.of(instr));

        while(true){
            comp.registerA = a;
            comp.registerB = b;
            comp.registerC = c;

            String test = comp.run();
            if (test.isEmpty()){
                a = a.add(BigInteger.ONE);
                continue;
            }

            if(test.equals(String.join(",", instr)))
                break;

            String[] sub = test.split(",");
            if(sub.length < i.size()){
                int s = sub.length;
                List<String> subInstr = i.subList(i.size()- s, i.size());
                if(String.join(",", subInstr).equals(String.join(",", sub))){
                    a = a.multiply(new BigInteger("8"));
                    continue;
                }
            }

            a = a.add(BigInteger.ONE);
        }

        System.out.println("Solution Stage 2: " + a);
    }
}
