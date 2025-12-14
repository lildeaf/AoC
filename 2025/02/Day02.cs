using AdventOfCode.helper;

namespace AdventOfCode._02;

public class Day02: Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "02";

    public Day02(bool test)
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
        var count = 0L;
        var ranges = this.lines.ElementAt(0).Split(",").ToList();
        ranges.ForEach(range =>
        {
            var rangeVals = range.Split("-");
            var start = long.Parse(rangeVals[0]) ;
            var end = long.Parse(rangeVals[1]) ;

            for (long i = start; i <= end; i++)
            {
                var x = i.ToString();
                var l = x.Length;
                if (l % 2 == 1) continue;
                var sec = x.Substring(l/2);
                var first = x.Substring(0, l/2);

                if (sec == first)
                {
                    count += i;
                }

            }
        });
        
        Console.WriteLine($"Solution stage 1: {count}");
    }

    public bool checkRep(long number, int length)
    {
        var x = number.ToString();
        var l = x.Length;
        if (l % length != 0) return false;

        var refString = x.Substring(0, length);
        for (int i = length; i < l; i += length)
        {
            var check = x.Substring(i, length);
            if (check != refString) return false;
        }
        
        return true;
    }

    public void solveStage2()
    {
        var count = 0L;
        var ranges = this.lines.ElementAt(0).Split(",").ToList();
        ranges.ForEach(range =>
        {
            var rangeVals = range.Split("-");
            var start = long.Parse(rangeVals[0]);
            var end = long.Parse(rangeVals[1]);

            for (long i = start; i <= end; i++)
            {
                var x = i.ToString();
                var l = x.Length;
                for (int j = 1; j <= l / 2; j++)
                {
                    if (checkRep(i, j))
                    {
                        count += i;
                        break;                        
                    }                    
                }
                
            }
        });
        
        Console.WriteLine($"Solution stage 2: {count}");
    }
}