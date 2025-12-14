using System.Text.RegularExpressions;
using AdventOfCode.helper;

namespace AdventOfCode._12;

public class Day12 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "12";

    public Day12(bool test)
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
        List<HashSet<(int, int)>> presents = new List<HashSet<(int, int)>>();
        List<((int,int), List<int>)> regions = new List<((int,int), List<int>)>();
        var index = 0;
        do
        {
            var line = lines[index++];
            var match = Regex.Match(line, @"(\d+)x(\d+): (.+)");
            if (match.Success)
            {
                var groups = match.Groups;
                var region = (int.Parse(groups[1].Value), int.Parse(groups[2].Value));
                var indices = groups[3].Value.Split(' ').Select(int.Parse).ToList();
                regions.Add((region, indices));
                continue;
            }

            HashSet<(int, int)> positions = new HashSet<(int, int)>();
            int y = 0;
            do
            {
                var presentLine = lines[index];
                for (int x = 0; x < presentLine.Length; ++x)
                {
                    if(presentLine[x] == '.')
                        continue;
                    
                    positions.Add((x, y));
                }
                y++;
            } while (this.lines[++index].Length > 0);
            
            presents.Add(positions);
            index++;

        } while (index < this.lines.Count);

        var result = 0;
        foreach (var region in regions)
        {
            var x = region.Item1.Item1;
            var y = region.Item1.Item2;
            
            var pX =  x / 3;
            var pY =  y / 3;

            var sum = region.Item2.Aggregate((a,b) => a+b);
            if(pX*pY >= sum)
                result++;
        }
        
        Console.WriteLine($"Solution stage 1: {result}");
        
    }

    public void solveStage2()
    {
        throw new NotImplementedException();
    }
}