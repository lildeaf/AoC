using AdventOfCode.helper;

namespace AdventOfCode._03;

public class Day03 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "03";

    public Day03(bool test)
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
        long res = 0;
        this.lines.ForEach(line =>
        {

            List<char> rev = new List<char>(line.Reverse());
            char high = rev[1], low = rev[0];

            for (int highestAffected = 2; highestAffected < rev.Count; highestAffected++)
            {
                char check = rev[highestAffected];
                //Console.WriteLine($"{check} ,  {high}{low} , {check > high && highestAffected > 0}");
                if (check >= high && highestAffected > 0)
                {
                    if(low <= high)
                        low = high;
                    high = check;
                }

                //Console.WriteLine($"{check} => {high}{low}");
            }
            
            res += int.Parse($"{high}{low}");
        });
        
        Console.WriteLine($"Stage 1 Solution: {res}");
    }

    Dictionary<string, long> cache = new Dictionary<string, long>();

    private long biggestNumPossible(String n, int digit)
    {
        string key = $"{n};{digit}";
        if (cache.ContainsKey(key))
        {
            return cache[key];
        }

        if (digit == 0)
        {
            cache.Add(key, 0);            
            return 0;
        }

        var current = long.Parse(n[0].ToString());
        var rest = n.Substring(1);
        var next1 = biggestNumPossible(n.Substring(1), digit - 1);
        next1 += current * (long)Math.Pow(10, digit-1);
        long next2 = 0;
        if(rest.Length >= digit)
            next2 = biggestNumPossible(n.Substring(1), digit);

        long returnVal = next1 > next2 ? next1 : next2;
        cache.Add(key, returnVal);
            
        return returnVal;
    }

    private int ACT_LENGTH = 2;
    public void solveStage2()
    {
        long res = 0;
        this.lines.ForEach(line =>
        {
            long test = biggestNumPossible(line, ACT_LENGTH);
            res += test;

        });
        Console.WriteLine($"Stage 2 Solution: {res}");
    }
}