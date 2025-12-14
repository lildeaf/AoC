namespace AdventOfCode.helper;

public class InputHelper
{
    public List<string> ReadLines(Boolean testing, String day)
    {
        var fileName = $"inputFiles{Path.DirectorySeparatorChar}{day}{Path.DirectorySeparatorChar}{(testing ? "example" : "input")}.txt";
        var lines = new List<string>();
        using (StreamReader reader = new StreamReader(fileName))
        {
            string line;
            while ((line = reader.ReadLine()) is not null)
            {
                lines.Add(line);
            }
        }

        return lines;
    }   
}