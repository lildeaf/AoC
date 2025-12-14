using AdventOfCode.helper;

namespace AdventOfCode._05;

public class Day05 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "05";

    public Day05(bool test)
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
        List<(ulong, ulong)> ranges = new List<(ulong, ulong)>();
        int index = 0;
        do
        {
            var line = lines[index++];
            var splitLine = line.Split('-');
            var low = ulong.Parse(splitLine[0]);
            var high = ulong.Parse(splitLine[1]);
            
            ranges.Add((low, high));
        } while (this.lines[index].Length != 0);

        index++;

        int count = 0;
        do
        {
            var line = lines[index++];
            var num = ulong.Parse(line);

            foreach (var range in ranges)
            {
                if (range.Item1 <= num && num <= range.Item2)
                {
                    count++;
                    break;
                }
            }            
            
        } while (index < lines.Count);
        
        Console.WriteLine($"Solution stage 1: {count}");
    }

    public void solveStage2()
    {
        HashSet<(ulong, ulong)> ranges = new HashSet<(ulong, ulong)>();
        int index = 0;
        do
        {
            var line = lines[index++];
            var splitLine = line.Split('-');
            var low = ulong.Parse(splitLine[0]);
            var high = ulong.Parse(splitLine[1]);

            HashSet<(ulong, ulong)> rangesToRemove = new HashSet<(ulong, ulong)>();
            bool skip = false;
            foreach (var range in ranges)
            {
                if (range.Item1 <= low && high <= range.Item2)
                {
                    skip = true;
                    break;
                }

                if (low <= range.Item1 && range.Item2 <= high)
                {
                    rangesToRemove.Add(range);
                    continue;
                }

                if (range.Item1 <= low && low <= range.Item2)
                {
                    low = range.Item1;
                    rangesToRemove.Add(range);
                    continue;
                }

                if (range.Item1 <= high && high <= range.Item2)
                {
                    high = range.Item2;
                    rangesToRemove.Add(range);
                    continue;
                }
            }
            if (skip) continue;
            
            foreach (var range in rangesToRemove)
            {
                ranges.Remove(range);
            }

            ranges.Add((low, high));
        } while (this.lines[index].Length != 0);
        ulong count = 0;
        foreach (var range in ranges)
        {
            count += (range.Item2 - range.Item1) + 1;
        }
        
        Console.WriteLine($"Solution stage 2: {count}");

    }
}