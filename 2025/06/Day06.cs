using System.Reflection.Metadata;
using System.Text.RegularExpressions;
using AdventOfCode.helper;

namespace AdventOfCode._06;

public class Day06 : Day
{
    private InputHelper helper;
    private bool test;

    private List<string> lines;
    
    private static string DAY = "06";

    public Day06(bool test)
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
        var operations = Regex.Split(this.lines[this.lines.Count - 1].Trim(), @"\s+");

        //var test = operations.Split(" ").ToList();
        List<ulong> results = new List<ulong>();
        foreach (var op in operations)
        {
            Console.WriteLine($"OP: {op}");
            var start = op == "+" ? 0 : 1;
            results.Add((ulong)start);
        }

        for (int i = 0; i < this.lines.Count - 1; i++)
        {
            var numbers = Regex.Split(this.lines[i].Trim(), @"\s+");
            
            for (int numIndex = 0; numIndex < numbers.Length; numIndex++)
            {

                var n = ulong.Parse(numbers[numIndex]);
                if (operations[numIndex] == "+")
                {
                    results[numIndex] = n + results[numIndex];
                }
                else
                {
                    results[numIndex] = n * results[numIndex];
                }
            }
        }

        ulong sum = 0;
        foreach (var result in results)
        {
            Console.WriteLine(result);
            sum += result;
        }
        
        Console.WriteLine($"Solution stage 1: {sum}");
    }

    public void solveStage2()
    {
        var operationMatches = Regex.Matches(this.lines[this.lines.Count - 1] + " ", @"\S\s+");
        ulong solution = 0;
        foreach (Match operationMatch in operationMatches)
        {
            //Console.WriteLine($"OP: {operationMatch.Value[0]}, {operationMatch.Length}");
            List<string> nums = new List<string>();
            var op = operationMatch.Value[0];
            var res = (ulong)(op == '+' ? 0 : 1);
            
            for (int i = 0; i < this.lines.Count - 1; i++)
            {
                var s = this.lines[i].Substring(operationMatch.Index,  operationMatch.Length-1);
                nums.Add(s);
            }
            //Console.WriteLine($"{String.Join(",", nums)}");
            for (int i = 0; i < operationMatch.Length - 1; i++)
            {
                ulong num = 0;
                ulong pow = 0;
                for (int e = nums.Count-1; e >= 0; e--)
                {
                    var c = nums[e][i];
                    if (c == ' ') continue;

                    num += ulong.Parse(c.ToString()) * (ulong)Math.Pow(10, pow++);
                }
                if(op == '+')
                    res += num;
                else
                    res *= num;
                //Console.WriteLine($"Nuimmber: {num}");
            }
            Console.WriteLine($"Res: {res}");
            solution += res;
            // result calc
        }
        Console.WriteLine($"Solution stage 2: {solution}");
    }
}