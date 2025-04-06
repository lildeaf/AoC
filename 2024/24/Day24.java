import java.math.BigInteger;
import java.util.*;

public class Day24 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "24";

    public Day24(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    private boolean resolveGate(String wire, HashMap<String, Boolean> wires, HashMap<String, String> gates){
        if (wires.containsKey(wire))
            return wires.get(wire);

        String[] gate = gates.get(wire).split(" ");
        boolean first = resolveGate(gate[0], wires, gates);
        boolean second = resolveGate(gate[2], wires, gates);
        boolean result = false;
        switch (gate[1]){
            case "AND" -> result = first && second;
            case "OR" -> result = first || second;
            case "XOR" -> result = first ^ second;
            default -> result = false;
        }
        gates.remove(wire);
        wires.put(wire, result);

        return result;
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        int i = 0;
        HashMap<String, Boolean> wires = new HashMap<>();

        do{
            String[] wire = this.lines.get(i).split(": ");
            wires.put(wire[0], wire[1].equals("1"));
        }while(!this.lines.get(++i).isEmpty());

        HashMap<String, String> gates = new HashMap<>();
        ArrayList<String> out = new ArrayList<>();
        for (i++; i < this.lines.size(); i++){
            String[] gate = this.lines.get(i).split(" -> ");
            gates.put(gate[1], gate[0]);
            if (gate[1].startsWith("z"))
                out.add(gate[1]);
        }

        Collections.sort(out);
        while (!gates.isEmpty()){
            String w = new ArrayList<>(gates.keySet()).getFirst();
            resolveGate(w, wires, gates);
        }

        BigInteger result = BigInteger.ZERO;
        for (int b = 0; b < out.size(); b++){
            if (!wires.get(out.get(b)))
                continue;
            result = result.add(BigInteger.TWO.pow(b));
        }

        System.out.println("Solution Stage 1: " + result);
    }

    private String swap(String swapWire, String currentWire, HashMap<String, String> gates){
        String gate = "";
        for (String g : gates.keySet()){
            String[] op = gates.get(g).split(" ");
            if (!currentWire.equals(op[0]) && !currentWire.equals(op[2]))
                continue;

            if (g.startsWith("z")){
                System.out.println("SWAPPING: " + g + " with " + swapWire);
                int n = Integer.parseInt(g.substring(1)) - 1;
                String swapOut = "z"+n;
                String s1 = gates.get(swapOut);
                String s2 = gates.get(swapWire);

                gates.put(swapWire, s1);
                gates.put(swapOut, s2);
                return swapOut;
            }
            gate = g;
        }

        return swap(swapWire, gate, gates);
    }

    private int checkAdder(HashMap<String, Boolean> wires, ArrayList<String> xVals, ArrayList<String> yVals, ArrayList<String> out){
        BigInteger result = BigInteger.ZERO;
        BigInteger x = BigInteger.ZERO;
        BigInteger y = BigInteger.ZERO;
        for (int b = 0; b < xVals.size(); b++){
            if (wires.get(xVals.get(b)))
                x = x.add(BigInteger.TWO.pow(b));

            if (wires.get(yVals.get(b)))
                y = y.add(BigInteger.TWO.pow(b));
        }
        BigInteger correctResult = x.add(y);
        String correct = correctResult.toString(2);

        for (int b = 0; b < out.size(); b++){
            if (!wires.get(out.get(b))){
                if (correct.charAt(out.size()-1-b) != '0'){
                    System.out.println("WRONG AT: " + b);
                    return b;
                }
                continue;
            }
            if (correct.charAt(out.size()-1-b) != '1'){
                System.out.println("WRONG AT: " + b);
                return b;
            }

            result = result.add(BigInteger.TWO.pow(b));
        }

        System.out.println(result.toString(2));
        System.out.println(correctResult.toString(2));
        return -1;
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int i = 0;
        HashMap<String, Boolean> wires = new HashMap<>();
        ArrayList<String> xValues = new ArrayList<>();
        ArrayList<String> yValues = new ArrayList<>();

        do{
            String[] wire = this.lines.get(i).split(": ");
            wires.put(wire[0], wire[1].equals("1"));
            if (wire[0].startsWith("x"))
                xValues.add(wire[0]);
            else
                yValues.add(wire[0]);
        }while(!this.lines.get(++i).isEmpty());

        HashMap<String, String> gates = new HashMap<>();
        ArrayList<String> out = new ArrayList<>();
        for (i++; i < this.lines.size(); i++){
            String[] gate = this.lines.get(i).split(" -> ");
            gates.put(gate[1], gate[0]);
            if (gate[1].startsWith("z"))
                out.add(gate[1]);
        }

        ArrayList<String> swappedGates = new ArrayList<>();

        for (String gate : gates.keySet()){
            String[] op = gates.get(gate).split(" ");
            if (gate.startsWith("z")){
                continue;
            }

            if(!op[0].startsWith("x") && !op[2].startsWith("x")){
                if(!op[1].equals("XOR"))
                    continue;

                swappedGates.add(gate);
                swappedGates.add(swap(gate, gate, gates));
            }
        }

        Collections.sort(xValues);
        Collections.sort(yValues);
        Collections.sort(out);
        HashMap<String, String> gates2 = new HashMap<>(gates);
        HashMap<String, Boolean> wires2 = new HashMap<>(wires);

        while (!gates.isEmpty()){
            String w = new ArrayList<>(gates.keySet()).getFirst();
            resolveGate(w, wires, gates);
        }

        int index = checkAdder(wires, xValues, yValues, out);
        for (String gate : gates2.keySet()){
            String[] op = gates2.get(gate).split(" ");
            if (!op[0].endsWith(String.format("%02d", index)))
                continue;

            swappedGates.add(gate);
        }

        Collections.sort(swappedGates);

        System.out.println("Solution Stage 2: " + String.join(",", swappedGates));
    }
}
