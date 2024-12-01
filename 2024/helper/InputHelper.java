import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class InputHelper {
    public ArrayList<String> readLines(boolean testing, String day){
        ArrayList<String> lines = new ArrayList<String>();
        try{
            String file = String.format("inputFiles/%s%s.txt", (testing ? "example" : "input"), day);
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
