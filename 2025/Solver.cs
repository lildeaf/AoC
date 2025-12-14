using AdventOfCode._01;
using AdventOfCode._02;
using AdventOfCode._03;
using AdventOfCode._04;
using AdventOfCode._05;
using AdventOfCode._06;
using AdventOfCode._07;
using AdventOfCode._08;
using AdventOfCode._09;
using AdventOfCode._10;
using AdventOfCode._11;
using AdventOfCode._12;
using AdventOfCode.helper;
class Solver
{
    static int Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.WriteLine("Wrong arguments");
            return -1;
        }

        Day day = null;
        int dayNum = Int16.Parse(args[0]);
        bool test = Boolean.Parse(args[1]);
        
        switch (dayNum)
        {
            case 1: day = new Day01(test); break;
            case 2: day = new Day02(test); break;
            case 3: day = new Day03(test); break;
            case 4: day = new Day04(test); break;
            case 5: day = new Day05(test); break;
            case 6: day = new Day06(test); break;
            case 7: day = new Day07(test); break;
            case 8: day = new Day08(test); break;
            case 9: day = new Day09(test); break;
            case 10: day = new Day10(test); break;
            case 11: day = new Day11(test); break;
            case 12: day = new Day12(test); break;
            default:
                Console.WriteLine("Second argument must be a number between 1 and 25"); 
                return -1; 
        }

        {
            var watch = System.Diagnostics.Stopwatch.StartNew();
            day.solveStage1();
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine($"Solved stage 1 in {elapsedMs}");
        }

        {
            var watch = System.Diagnostics.Stopwatch.StartNew();
            day.solveStage2();
            watch.Stop();
            var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine($"Solved stage 2 in {elapsedMs}");
        }

        return 0;
    }
};

