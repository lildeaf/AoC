using AdventOfCode.helper;

namespace AdventOfCode._07;

public class Day07 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "07";
    private int maxX = 0;
    private int maxY = 0;
    public Day07(bool test)
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

    Dictionary<(int,int), ulong> cache = new Dictionary<(int,int), ulong>();
    
    private ulong countSplit((int, int) current, HashSet<(int,int)> splitters)
    {
        if(current.Item2 == maxY)
            return 0;

        if (this.cache.ContainsKey(current))
            return 0;

        ulong result;
        if (splitters.Contains(current))
        {
            result = 1 + countSplit((current.Item1-1, current.Item2), splitters) + countSplit((current.Item1+1, current.Item2), splitters);
            this.cache.Add(current, result);
            return result;
        }
        
        result = countSplit((current.Item1, current.Item2 + 1), splitters);
        return result;
    }
    
    private ulong countPaths((int, int) current, HashSet<(int,int)> splitters)
    {
        if(current.Item2 == maxY)
            return 1;

        if (this.cache.ContainsKey(current))
            return this.cache[current];

        ulong result;
        if (splitters.Contains(current))
        {
            result = countPaths((current.Item1-1, current.Item2), splitters) + countPaths((current.Item1+1, current.Item2), splitters);
            this.cache.Add(current, result);
            return result;
        }
        
        result = countPaths((current.Item1, current.Item2 + 1), splitters);
        return result;
    }

    
    public void solveStage1()
    {
        var start = this.lines[0].IndexOf('S');
        (int,int) position = (start, 0);
        HashSet<(int,int)> splitters = new HashSet<(int,int)>();
        for (var y = 1; y < this.lines.Count; y++)
        {
            var line = this.lines[y];
            for (var x = 0; x < line.Length; x++)
            {
                if(line[x] == '^') splitters.Add((x, y));
            }
        }
        
        ulong solution = countSplit(position, splitters);
        Console.WriteLine($"Solution stage 1: {solution}");
    }

    public void solveStage2()
    {
        this.cache.Clear();
        var start = this.lines[0].IndexOf('S');
        (int,int) position = (start, 0);
        HashSet<(int,int)> splitters = new HashSet<(int,int)>();
        for (var y = 1; y < this.lines.Count; y++)
        {
            var line = this.lines[y];
            for (var x = 0; x < line.Length; x++)
            {
                if(line[x] == '^') splitters.Add((x, y));
            }
        }
        
        ulong solution = countPaths(position, splitters);
        Console.WriteLine($"Solution stage 2: {solution}");
    }
}