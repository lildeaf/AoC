import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class InputHelper {
    private final String separator = System.getProperty("file.separator");

    public ArrayList<String> readLines(boolean testing, String day){
        ArrayList<String> lines = new ArrayList<>();
        try{
            String file = "inputFiles" + separator + day + separator + (testing ? "example" : "input") + ".txt";
            File myObj = new File(file);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()){
                String line = myReader.nextLine();
                lines.add(line);
            }
        } catch (FileNotFoundException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
            return null;
        }

        return lines;
    }
}
