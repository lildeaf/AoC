import java.util.*;

public class Day23 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "23";

    public Day23(boolean testing){
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if(this.lines == null){
            System.exit(-1);
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        HashMap<String, HashSet<String>> connections = new HashMap<>();

        for (String line: this.lines){
            String[] pcs = line.split("-");

            HashSet<String> conn1 = connections.getOrDefault(pcs[0], new HashSet<>());
            HashSet<String> conn2 = connections.getOrDefault(pcs[1], new HashSet<>());

            conn1.add(pcs[1]);
            conn2.add(pcs[0]);

            connections.put(pcs[0], conn1);
            connections.put(pcs[1], conn2);
        }

        System.out.println(connections);
        HashSet<String> threeConns = new HashSet<>();

        for (String pc : connections.keySet()){
            if (!pc.startsWith("t"))
                continue;

            //System.out.println(pc);
            HashSet<String> conn1 = connections.get(pc);
            for (String c1 : conn1){
                HashSet<String> conn2 = connections.get(c1);
                for (String c2 : conn2){
                    if (!conn1.contains(c2))
                        continue;

                    ArrayList<String> net = new ArrayList<>(List.of(new String[]{pc, c1, c2}));
                    Collections.sort(net);
                    threeConns.add(String.join("-", net));
                }
            }
        }

        System.out.println(threeConns);
        System.out.println("Solution Stage 1: " + threeConns.size());
    }

    private HashSet<String> BronKerbosch(HashSet<String> R, HashSet<String> P, HashSet<String> X, HashMap<String, HashSet<String>> connections){
        if (P.isEmpty() && X.isEmpty())
            return R;

        HashSet<String> maxSet = new HashSet<>();
        HashSet<String> R1 = new HashSet<>(R);
        HashSet<String> P1 = new HashSet<>(P);
        HashSet<String> X1 = new HashSet<>(X);

        for (String pc : P){
            HashSet<String> R2 = new HashSet<>(R1);
            HashSet<String> P2 = new HashSet<>(P1);
            HashSet<String> X2 = new HashSet<>(X1);
            R2.add(pc);
            HashSet<String> neighbors = connections.get(pc);
            P2.retainAll(neighbors);
            X2.retainAll(neighbors);
            HashSet<String> tmpMax = BronKerbosch(R2, P2, X2, connections);
            P1.remove(pc);
            X1.add(pc);
            if (tmpMax.size() > maxSet.size())
                maxSet = tmpMax;
        }

        return maxSet;
    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        int sum = 0;
        HashMap<String, HashSet<String>> connections = new HashMap<>();

        for (String line: this.lines){
            String[] pcs = line.split("-");

            HashSet<String> conn1 = connections.getOrDefault(pcs[0], new HashSet<>());
            HashSet<String> conn2 = connections.getOrDefault(pcs[1], new HashSet<>());

            conn1.add(pcs[1]);
            conn2.add(pcs[0]);

            connections.put(pcs[0], conn1);
            connections.put(pcs[1], conn2);
        }

        HashSet<String> test = BronKerbosch(new HashSet<>(), new HashSet<>(connections.keySet()), new HashSet<>(), connections);
        System.out.println(test);

        ArrayList<String> lan = new ArrayList<>(test);
        Collections.sort(lan);

        System.out.println("Solution Stage 2: " + String.join(",", lan));
    }
}
