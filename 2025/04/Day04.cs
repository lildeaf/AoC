using AdventOfCode.helper;

namespace AdventOfCode._04;

public class Day04 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "04";

    private int maxX = 0;
    private int maxY = 0;
    public Day04(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        maxX = this.lines[0].Length;
        maxY = this.lines.Count;
    }

    public bool checkSurrounding(int x, int y)
    {
        int count = 0;
        for (var xDiff = -1; xDiff < 2; xDiff++)
        {
            for (var yDiff = -1; yDiff < 2; yDiff++)
            {
                if (xDiff == 0 && yDiff == 0)
                    continue;

                var checkX = x +  xDiff;
                var checkY = y +  yDiff;
                
                if(checkX < 0 || checkX >= maxX || checkY < 0 || checkY >= maxY)
                    continue;
                
                if(this.lines[checkY][checkX] == '.')
                    continue;
                if (++count >= 4)
                    return false;
            }        
        }
        
        return true;
    }
    
    public bool checkSurrounding2(int x, int y, HashSet<(int, int)> rolls)
    {
        int count = 0;
        for (var xDiff = -1; xDiff < 2; xDiff++)
        {
            for (var yDiff = -1; yDiff < 2; yDiff++)
            {
                if (xDiff == 0 && yDiff == 0)
                    continue;

                var checkX = x +  xDiff;
                var checkY = y +  yDiff;
                
                if(checkX < 0 || checkX >= maxX || checkY < 0 || checkY >= maxY)
                    continue;

                if(!rolls.Contains((checkX,checkY)))
                    continue;
                if (++count >= 4)
                    return false;
            }        
        }
        
        return true;
    }
    public void solveStage1()
    {
        var count = 0;
        for (var y = 0; y < this.lines.Count; y++)
        {
            var line = this.lines[y];
            for (var x = 0; x < line.Length; x++)
            {
                var c = line[x];
                if (c != '@')
                    continue;

                if (checkSurrounding(x, y))
                    count++;

            }
        }
        Console.WriteLine($"Solution stage 1:  {count}");                    

    }

    
    public void solveStage2()
    {
        
        HashSet<(int, int)> rolls = new HashSet<(int, int)>();

        for (var y = 0; y < this.lines.Count; y++)
        {
            var line = this.lines[y];
            for (var x = 0; x < line.Length; x++)
            {
                var c = line[x];
                if (c != '@')
                    continue;
                
                rolls.Add((x, y));
            }
        }
        
        HashSet<(int, int)> currRolls = new HashSet<(int, int)>(rolls);
        var count = 0;
        do
        {
            rolls = new HashSet<(int, int)>(currRolls);
            foreach (var valueTuple in rolls)
            {
                if (checkSurrounding2(valueTuple.Item1, valueTuple.Item2, rolls))
                {
                    count++;
                    currRolls.Remove(valueTuple);
                }
                    
            }
        } while (currRolls.Count != rolls.Count);
        Console.WriteLine($"Solution stage 2:  {count}");
    }
}