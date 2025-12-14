using AdventOfCode.helper;

namespace AdventOfCode._01;

public class Day01 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "01";

    public Day01(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        
    }
    public void solveStage1()
    {
        var dial = 50;
        var count = 0;
        this.lines.ForEach(line =>
        {
            int n = Int32.Parse(line.Substring(1));

            if (line[0] == 'L')
                dial -= n;
            else 
                dial += n;

            count += dial % 100 == 0 ? 1 : 0;
            
        });

        Console.WriteLine($"Solution stage 1: {count}");
    }

    public void solveStage2()
    {
        var dial = 50;
        var count = 0;
        this.lines.ForEach(line =>
        {
            int n = Int32.Parse(line.Substring(1));
            var newDial = dial;
            var hundreds = n / 100;
            n -= 100 * hundreds;
            count += hundreds;

            
            if (line[0] == 'L')
            {
                newDial = (dial + 100 - n) % 100;
                count += ((dial % 100 != 0) && newDial > dial) || (newDial % 100 == 0) ? 1 : 0;
            }
            else
            {
                newDial = (dial + 100+n) % 100;
                count += ((dial % 100 != 0) && newDial < dial) || (newDial % 100 == 0) ? 1 : 0;
            }
            dial = newDial;
        });

        Console.WriteLine($"Solution stage 2: {count}");
    }
}