using System.Text.RegularExpressions;
using AdventOfCode.helper;

namespace AdventOfCode._11;

public class Day11 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "11";

    public Day11(bool test)
    {
        this.test = test;
        this.helper = new InputHelper();
        this.lines = helper.ReadLines(this.test, DAY);
        if (this.lines.Count == 0) {
            System.Environment.Exit(-1);
        }
        
    }

    private ulong countPaths(Dictionary<string, HashSet<string>> connections, string current)
    {
        if (current == "out")
            return 1;
        
        ulong sum = 0;
        var next = connections[current];
        foreach (var se in next)
        {
            sum += countPaths(connections, se);
        }        
        
        return sum;
    }
    
    Dictionary<string, (ulong,ulong,ulong, ulong)> cache =  new Dictionary<string, (ulong,ulong,ulong, ulong)>();
    
    private (ulong,ulong,ulong, ulong) countPathsIncluding(Dictionary<string, HashSet<string>> connections, string current)
    {
        if (current == "out")
        {
            return (0, 0, 0, 1);
        }
        
        if(cache.ContainsKey(current))
            return cache[current];
        
        var next = connections[current];
        (ulong, ulong, ulong, ulong) sum = (0,0,0,0);
        foreach (var se in next)
        {
            var res = countPathsIncluding(connections, se);
            sum.Item1 += res.Item1;
            sum.Item2 += res.Item2;
            sum.Item3 += res.Item3;
            sum.Item4 += res.Item4;
        }

        if (current == "dac")
        {
            sum = (sum.Item4, 0, sum.Item2, 0);
        }

        if (current == "fft")
        {
            sum = (0, sum.Item4, sum.Item1, 0);
        }
        
        cache.Add(current, sum);

        return sum;
    }
    
    public void solveStage1()
    {
        Dictionary<string, HashSet<string>> connections = new Dictionary<string, HashSet<string>>();

        foreach (var line in this.lines)
        {
            var match = Regex.Match(line, @"(.+)(: )(.+)");
            var device = match.Groups[1].Value;
            var outputs = match.Groups[3].Value.Split(" ").ToHashSet();
            connections[device] = outputs; 
        }

        var s = countPaths(connections, "you");
        Console.WriteLine($"Solution stage 1: {s}");
    }

    public void solveStage2()
    {
        Dictionary<string, HashSet<string>> connections = new Dictionary<string, HashSet<string>>();

        foreach (var line in this.lines)
        {
            var match = Regex.Match(line, @"(.+)(: )(.+)");
            var device = match.Groups[1].Value;
            var outputs = match.Groups[3].Value.Split(" ").ToHashSet();
            connections[device] = outputs; 
        }

        var s = countPathsIncluding(connections, "svr");
        Console.WriteLine($"Solution stage 2: {s.Item3}");
    }
}