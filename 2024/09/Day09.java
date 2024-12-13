import java.math.BigInteger;
import java.util.*;

public class Day09 implements Day{
    private final InputHelper inputHelper;
    final ArrayList<String> lines;

    private static final String DAY = "09";

    public Day09(boolean testing) {
        this.inputHelper = new InputHelper();
        this.lines = this.inputHelper.readLines(testing, DAY);
        if (this.lines == null) {
            System.exit(-1);
        }
    }

    private static class DiskSpace{
        final int id;
        int count;

        //stage 2
        int startIndex;

        public DiskSpace(int id, int count){
            this.id = id;
            this.count = count;
        }

        //stage 2
        public DiskSpace(int id, int count, int startIndex){
            this.id = id;
            this.count = count;
            this.startIndex = startIndex;
        }


        public boolean reduce(){
            return --this.count == 0;
        }

        //stage 2
        public BigInteger getChecksum() {
            BigInteger check = new BigInteger("0");
            while (this.count-- > 0){
                check = check.add(new BigInteger(String.valueOf((long)this.id * this.startIndex++)));
            }

            return check;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            Day09.DiskSpace that = (Day09.DiskSpace) o;
            return id == that.id;
        }

        @Override
        public int hashCode() {
            return id;
        }

        @Override
        public String toString() {
            return id + ": " + count;
        }
    }

    @Override
    public void solveStage1() {
        System.out.println("Solving Stage 1...");
        String diskMap = this.lines.getFirst();

        Deque<DiskSpace> diskFiles = new ArrayDeque<>();
        Queue<Integer> diskFreeSpace = new LinkedList<>();

        for(int i = 0; i < diskMap.length(); i++){
            int id = i/2;
            int count = Integer.parseInt(String.valueOf(diskMap.charAt(i)));

            if(i%2 == 0){
                diskFiles.add(new DiskSpace(id, count));
            }else{
                diskFreeSpace.add(count);
            }
        }

        long checksum = 0;
        long index = 0;
        while (!diskFiles.isEmpty()){
            DiskSpace current = diskFiles.pollFirst();

            for(int i = 0; i < current.count; i++){
                checksum += current.id * index++;
            }

            if(diskFreeSpace.isEmpty()){
                continue;
            }

            Integer free = diskFreeSpace.poll();
            for (; free > 0; free--){
                DiskSpace last = diskFiles.peekLast();
                if(last == null)
                    break;

                checksum += last.id * index++;
                if(last.reduce())
                    diskFiles.removeLast();
            }
        }

        System.out.println("Solution Stage 1: " + checksum);

    }

    @Override
    public void solveStage2() {
        System.out.println("Solving Stage 2...");
        String diskMap = this.lines.getFirst();

        Deque<DiskSpace> diskFiles = new ArrayDeque<>();
        ArrayList<DiskSpace> diskFreeSpace = new ArrayList<>();

        int index = 0;
        for(int i = 0; i < diskMap.length(); i++){
            int id = i/2;
            int count = Integer.parseInt(String.valueOf(diskMap.charAt(i)));

            if(i%2 == 0){
                diskFiles.add(new DiskSpace(id, count, index));
            }else{
                diskFreeSpace.add(new DiskSpace(-1, count, index));
            }
            index += count;
        }

        BigInteger checksum = new BigInteger(String.valueOf(0));
        while (!diskFiles.isEmpty()){
            DiskSpace current = diskFiles.pollLast();
            int i = 0;
            for(; i < diskFreeSpace.size(); i++){
                DiskSpace free = diskFreeSpace.get(i);
                if(free.startIndex < current.startIndex && free.count >= current.count){
                    break;
                }
            }
            if (i == diskFreeSpace.size()){
                //nothing found
                checksum = checksum.add(current.getChecksum());
                continue;
            }

            DiskSpace free = diskFreeSpace.get(i);
            current.startIndex = free.startIndex;
            free.count -= current.count;
            free.startIndex += current.count;
            checksum = checksum.add(current.getChecksum());
            if(free.count == 0){
                diskFreeSpace.remove(i);
            }
        }
        System.out.println("Solution Stage 2: " + checksum);
    }
}
